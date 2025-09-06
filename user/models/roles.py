# user/models/role.py
from django.db import models

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)  # e.g., Admin, Staff, SuperAdmin
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
