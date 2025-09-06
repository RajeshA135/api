from ..models.users import CustomUser
from rest_framework import serializers
from ..models.roles import Role  # Ensure Role model is imported
from ..serializers.role import RoleSerializer
class SignupSerializer(serializers.ModelSerializer):
    # role=RoleSerializer(read_only=True)
    # role_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Role.objects.all(),
    #     source='role',
    #     write_only=True
    # )
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'is_staff', 'role','role_id']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        role = validated_data.get('role')  # This should be a Role instance or ID
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=role  # Pass role here
        )
        user.is_staff = validated_data.get('is_staff', False)
        user.save()
        return user
