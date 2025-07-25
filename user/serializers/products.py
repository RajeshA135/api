from django.contrib.auth.models import User
from rest_framework import serializers
from ..models.products import Product
class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'code', 'desc', 'created_by']
    