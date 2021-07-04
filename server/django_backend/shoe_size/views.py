from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import OwnShoes, ShoesDataset
from .serializers import OwnShoesSerializer
from django.views.decorators.csrf import csrf_exempt
from social_login.jwt import jwt_authorization

# Create your views here.

# multiple lookup fields
class MultipleFieldLookupMixin:
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: # Ignore empty fields.
                filter[field] = self.kwargs[field]
        
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj

# OwnShoes List
class OwnShoesListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    lookup_field = 'user_pk'
    queryset = OwnShoes.objects.all()
    serializer_class = OwnShoesSerializer
    
    @csrf_exempt
    @jwt_authorization
    def get(self, request, *args, **kwargs):
        offset = None
        if request.GET.get('offset'):
            offset = int(request.GET.get('offset'))
        
        limit = None
        if request.GET.get('limit'):
            limit = int(request.GET.get('limit'))
        
        OwnShoes_obj = OwnShoes.objects.filter(user_pk=request.user)[offset:limit]
        datas = []
        for m in OwnShoes_obj:
            serializer = self.serializer_class(m)
            datas.append(serializer.data)
        return JsonResponse({'message': 'OWNSHOES LISTING SUCCESS', 'count': len(OwnShoes_obj), 'data': datas}, status=200)

# OwnShoes Create
class OwnShoesCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = OwnShoes.objects.all()
    serializer_class = OwnShoesSerializer
    
    @csrf_exempt
    @jwt_authorization
    def post(self, request, *args, **kwargs):
        request.data['user_pk'] = int(str(request.user))
        self.create(request, *args, **kwargs)
        return JsonResponse({'message': 'OWNSHOES CREATION SUCCESS'}, status=201)

class OwnShoesUpdateAPIView(UpdateAPIView):
    permission_classes = [AllowAny]
    lookup_field = 'id'
    queryset = OwnShoes.objects.all()
    serializer_class = OwnShoesSerializer
    
    @csrf_exempt
    @jwt_authorization
    def put(self, request, *args, **kwargs):
        request.data['user_pk'] = int(str(request.user))
        self.update(request, *args, **kwargs)
        return JsonResponse({'message': 'OWNSHOES UPDATE SUCCESS'}, status=201)

class OwnShoesDeleteAPIView(DestroyAPIView):
    permission_classes = [AllowAny]
    lookup_field = 'id'
    queryset = OwnShoes.objects.all()
    serializer_class = OwnShoesSerializer
    
    @csrf_exempt
    @jwt_authorization
    def delete(self, request, *args, **kwargs):
        request.data['user_pk'] = int(str(request.user))
        self.destroy(request, *args, **kwargs)
        return JsonResponse({'message': 'OWNSHOES DELETION SUCCESS'}, status=201)