from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, kakao_id, kakao_nickname, password=None, **extra_fields):
        """
        주어진 카카오아이디값, 닉네임으로 개인정보로 User 인스턴스 생성
        """
        user = self.model(kakao_id=kakao_id, kakao_nickname=kakao_nickname)
        user.set_unusable_password()
        user.save()
        return user
    
    def create_superuser(self, kakao_id, kakao_nickname, password=None, **extra_fields):
        """
        주어진 카카오아이디값, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여한다. 
        """
        superuser = self.create_user(kakao_id=kakao_id, kakao_nickname=kakao_nickname, password=password)
        superuser.is_staff= True
        superuser.is_admin = True
        superuser.is_active = True
        superuser.is_superuser = True
        superuser.save()
        return superuser

class User(AbstractBaseUser, PermissionsMixin):
    # basic form
    email = models.EmailField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    # state
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    # custom
    user_pk = models.AutoField(primary_key=True)
    foot_size = models.IntegerField(null=True, blank=True)
    ## kakao
    kakao_id = models.IntegerField(unique=True, null=True, blank=True)
    kakao_nickname = models.CharField(max_length=40, null=True, blank=True)
    ## naver
    pass
    # setting
    USERNAME_FIELD = None
    if kakao_id:
        USERNAME_FIELD = 'kakao_id'
    REQUIRED_FIELDS = ['kakao_nickname']
    objects = UserManager()
    
    def __str__(self):
        return str(self.user_pk)
    
    class Meta:
        db_table = 'User'