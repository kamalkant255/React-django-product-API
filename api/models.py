from django.db import models

# Create your models here.

class Product(models.Model):
     title=models.CharField(max_length=100)
     price=models.CharField(max_length=100)
     image=models.ImageField(max_length=300)

     description=models.CharField(max_length=100)
