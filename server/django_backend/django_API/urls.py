"""django_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from social_login import logins, tests
from shoe_size import views
from .settings import DEBUG
import debug_toolbar

urlpatterns = [
    path('admin', admin.site.urls),
    # login
    path('accounts/login/kakao', logins.kakao_login, name='kakao_login'),
    # OwnShoes
    path('ownshoes/list', views.OwnShoesListAPIView.as_view(), name='ownshoes_list'),
    path('ownshoes/create', views.OwnShoesCreateAPIView.as_view(), name='ownshoes_create'),
    path('ownshoes/update/<id>', views.OwnShoesUpdateAPIView.as_view(), name='ownshoes_update'),
    path('ownshoes/delete/<id>', views.OwnShoesDeleteAPIView.as_view(), name='ownshoes_delete'),
]

# Dev
if DEBUG == True:
    dev = [
        # kakao login test
        path('accounts/login/kakao/test', tests.kakao_login_test, name='kakao_login_test'),
        path('accounts/login/kakao/callback/test', tests.kakao_callback_test, name='kakao_callback_test'),
        # django-debug-toolbar
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += dev