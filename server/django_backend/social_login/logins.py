from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .jwt import jwt_publish, jwt_authorization
from .models import User
import requests

# Create your views here.


@csrf_exempt
@require_http_methods(['GET'])
def kakao_login(self):
    # access_token
    try:
        access_token = request.headers['Token']
    except KeyError:
        return JsonResponse({'message': 'HEADERS KAKAO TOKEN KEY ERROR'}, status=400)
    # profile
    profile_url = 'https://kapi.kakao.com/v2/user/me'
    headers = {'Authorization' : f'Bearer {access_token}'}
    profile_request = requests.get(profile_url, headers=headers)
    profile_json = profile_request.json()
    try:
        kakao_id = profile_json['id']
        kakao_nickname = profile_json['properties']['nickname']
    except KeyError:
        return JsonResponse({'message': 'KAKAO API PROFILE KEY ERROR'}, status=400)
    # User, access_jwt
    User_search = User.objects.filter(kakao_id=kakao_id)
    access_jwt = jwt_publish(kakao_id, access_token)
    if User_search:
        pass
    else:
        User.objects.create(kakao_id=kakao_id, kakao_nickname=kakao_nickname)
    
    # response = JsonResponse({'message': 'KAKAO LOGIN SUCESS'}, status=201)
    # response.set_cookie('access_token', value=access_token, max_age=60*60*24*7, expires='None', path='/', domain='None', httponly=False, samesite='None')
    # response.set_cookie('access_jwt', value=access_jwt, max_age=60*60*24*7, expires='None', path='/', domain='None', httponly=False, samesite='None')
    return JsonResponse({'message': 'KAKAO LOGIN SUCESS', 'Authorization': access_jwt}, status=201)

# def naver_login(self):
#     pass