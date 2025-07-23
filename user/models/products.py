from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=20)
    code = models.IntegerField()
    desc = models.CharField(max_length=100)
