from django.db import models

class Organization(models.Model):
    org_name = models.CharField(max_length=20)
    org_desc = models.CharField(max_length=100)
    def __str__(self):
        return self.org_name