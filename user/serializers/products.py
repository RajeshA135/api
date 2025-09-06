from rest_framework import serializers
from ..models.products import Product
from user.serializers.users import UserSerializer
from ..serializers.organization import OrganizationSerializer


class ProductSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    created_by_id = serializers.PrimaryKeyRelatedField(
        source="created_by",
        queryset=Product._meta.get_field("created_by").remote_field.model.objects.all(),
        write_only=True,
        required=False,
    )

    organization = OrganizationSerializer(read_only=True)
    organization_id = serializers.PrimaryKeyRelatedField(
        source="organization",
        queryset=Product._meta.get_field("organization").remote_field.model.objects.all(),
        write_only=True,
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "organization",
            "organization_id",
            "created_by",
            "created_by_id",
            "created_at",
        ]
