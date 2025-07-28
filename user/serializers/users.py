from ..models.users import CustomUser
from ..models.roles import Role
from rest_framework import serializers
from .role import RoleSerializer


class UserSerializer(serializers.ModelSerializer):
        role = RoleSerializer(read_only=True)
        email_name = serializers.CharField(read_only=True)
        email_domain = serializers.SerializerMethodField(read_only=True)
        class Meta:
            model = CustomUser
            fields = ['id', 'username', 'email', 'password','is_staff', 'role', 'email_name', 'email_domain']
            extra_kwargs = {'password': {'write_only': True}}
            # depth = 1
        
        def get_email_name(self, obj):
            return obj.email.split('@')[0]
        
        def get_email_domain(self, obj):
            return obj.email.split('@')[1]
        
        def create(self, validated_data):
            # Use Django's built-in method to hash passwords
            user = CustomUser.objects.create_user(**validated_data)
            return user

        def update(self, instance, validated_data):
            password = validated_data.pop('password', None)
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            if password:
                instance.set_password(password)
            instance.save()
            return instance