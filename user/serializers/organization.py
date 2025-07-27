from rest_framework import serializers
from ..models.Organization import Organization
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'
    