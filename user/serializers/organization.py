from rest_framework import serializers
from..models.organization import Organization
from user.serializers.users import UserSerializer


class OrganizationSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    created_by_id = serializers.PrimaryKeyRelatedField(
        source="created_by",
        queryset=Organization._meta.get_field("created_by").remote_field.model.objects.all(),
        write_only=True,
        required=False,
    )

    class Meta:
        model = Organization
        fields = ["id", "org_name", "org_desc", "parent", "created_by", "created_by_id", "created_at"]
