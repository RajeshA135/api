# user/models/users.py
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from ..models.roles import Role

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    # extra fields if needed
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} ({self.role})"
