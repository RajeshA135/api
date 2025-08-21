from rest_framework import serializers
from ..models.organization import Organization
from rest_framework import serializers
from ..models import Organization

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ["id", "org_name", "org_desc", "parent", "created_by"]

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user if request else None

        # create org without parent first
        org = Organization.objects.create(**validated_data)

        # set parent to self.id
        if org.parent is None:
            org.parent = org

        # set created_by to logged in user
        if user and org.created_by is None:
            org.created_by = user

        org.save()
        return org
