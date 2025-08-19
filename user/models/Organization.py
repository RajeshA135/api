from django.db import models
from ..models.users import CustomUser  # adjust import to your project

class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    org_name = models.CharField(max_length=20)
    org_desc = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )
    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_organizations"
    )

    def __str__(self):
        return self.org_name
