# products/models/products.py
from django.db import models
from user.models.users import CustomUser
from ..models.organization import Organization

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    # org in which product belongs
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="products")

    # who added product
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="products")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.organization.org_name})"
