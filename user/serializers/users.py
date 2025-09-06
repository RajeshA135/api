from rest_framework import serializers
from user.models.users import CustomUser
from user.serializers.role import RoleSerializer


class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)  # show role details
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser._meta.get_field("role").remote_field.model.objects.all(),
        source="role",
        write_only=True,
        required=False
    )

    email_name = serializers.SerializerMethodField(read_only=True)
    email_domain = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_staff",
            "role",
            "role_id",
            "email_name",
            "email_domain",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def get_email_name(self, obj):
        return obj.email.split("@")[0] if obj.email else None

    def get_email_domain(self, obj):
        return obj.email.split("@")[1] if obj.email else None

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = CustomUser(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
