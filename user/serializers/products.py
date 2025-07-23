from django.contrib.auth.models import User
from rest_framework import serializers
from ..models.products import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    