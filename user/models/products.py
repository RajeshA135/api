from django.db import models
from ..models.users import CustomUser

class Product(models.Model):
    name = models.CharField(max_length=20)
    code = models.IntegerField()
    desc = models.CharField(max_length=100)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products')
