from django.conf import settings
from django.db import models

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
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_organizations"
    )

    def __str__(self):
        return self.org_name
