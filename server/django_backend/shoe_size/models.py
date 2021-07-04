from django.db import models
from social_login.models import User
# Create your models here.

class OwnShoes(models.Model):
    id = models.AutoField(primary_key=True)
    user_pk = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, db_column='user_pk')
    brand = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255, unique=True)
    shoe_size = models.CharField(max_length=255)
    size_standard = models.CharField(max_length=4)
    
    def __str__(self):
        return str(self.model_num)
    
    class Meta:
        db_table = 'OwnShoes'

class ShoesDataset(models.Model):
    id = models.AutoField(primary_key=True)
    reviewer_id = models.CharField(max_length=255)
    gender = models.BooleanField(null=True, blank=True)
    height = models.CharField(max_length=255, null=True, blank=True)
    foot_size = models.CharField(max_length=255, null=True, blank=True)
    brand = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255, unique=True)
    shoe_size = models.CharField(max_length=255)
    size_standard = models.CharField(max_length=4)
    
    
    def __str__(self):
        return str(self.model_num)
    
    class Meta:
        db_table = 'ShoesDataset'