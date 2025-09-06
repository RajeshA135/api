# organization/models/organization.py
from django.db import models
from user.models.users import CustomUser

class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    org_name = models.CharField(max_length=100, unique=True)
    org_desc = models.TextField(blank=True, null=True)

    # Parent organization (for main/sub branches)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )

    # who created this org
    created_by = models.ForeignKey(
        CustomUser, null=True, blank=True, on_delete=models.SET_NULL, related_name="created_orgs"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.org_name
