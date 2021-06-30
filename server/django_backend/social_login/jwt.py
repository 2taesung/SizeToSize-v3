from django.http import JsonResponse
from social_login.models import User
from django_API.my_settings import JWT_SETTING
import jwt
import datetime

def jwt_publish(social_id):
    jwt_expiration = datetime.datetime.utcnow() + datetime.timedelta(seconds=60*60*6)
    access_jwt = jwt.encode({'exp': jwt_expiration, 'social_id': social_id}, key=JWT_SETTING['JWT_SECRET_KEY'], algorithm=JWT_SETTING['JWT_ALGORITHM'])
    return access_jwt

def jwt_authorization(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            # access_token
            # try:
            #     access_token = request.headers['Token']
            # except KeyError:
            #     return JsonResponse({'message': 'HEADERS JWT TOKEN KEY ERROR'}, status=400)
            # access_jwt
            try:
                Authorization = request.headers['Authorization']
            except KeyError:
                return JsonResponse({'message': 'HEADERS JWT AUTHORIZATION KEY ERROR'}, status=400)
            try:
                access_jwt = Authorization.split('JWT ')[1]
            except:
                return JsonResponse({'message': 'JWT AUTHORIZATION INVALID FORM ERROR'}, status=400)
            # decode
            payload = jwt.decode(access_jwt, key=JWT_SETTING['JWT_SECRET_KEY'], algorithms=JWT_SETTING['JWT_ALGORITHM'])
            login_user = User.objects.get(kakao_id=payload['social_id'])
            request.user = login_user
            return func(self, request, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': 'JWTOKEN EXPIRED'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'message': 'INVALID JWTOKEN'}, status=401)
    return wrapper