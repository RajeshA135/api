# organization/models/org_user.py
from django.db import models
from user.models.users import CustomUser
from .organization import Organization

class OrgUser(models.Model):
    id = models.AutoField(primary_key=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="org_users")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_orgs")
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('organization', 'user')  # prevent duplicate assignments

    def __str__(self):
        return f"{self.user.username} -> {self.organization.org_name}"
