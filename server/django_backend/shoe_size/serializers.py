from rest_framework import serializers
from .models import OwnShoes

class OwnShoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnShoes
        fields = (
            'id',
            'user_pk',
            'brand',
            'model_num',
            'shoe_size',
            'size_standard',
            )