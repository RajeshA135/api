from rest_framework import serializers
from ..models.org_user import OrgUser
from user.serializers.users import UserSerializer
from ..serializers.organization import OrganizationSerializer


class OrgUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        source="user", queryset=OrgUser._meta.get_field("user").remote_field.model.objects.all(), write_only=True
    )

    organization = OrganizationSerializer(read_only=True)
    organization_id = serializers.PrimaryKeyRelatedField(
        source="organization", queryset=OrgUser._meta.get_field("organization").remote_field.model.objects.all(), write_only=True
    )

    class Meta:
        model = OrgUser
        fields = ["id", "organization", "organization_id", "user", "user_id", "is_active"]
