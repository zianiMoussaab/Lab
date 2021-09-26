from django.db import models

# Create your models here.

class lab(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=150)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    region = models.CharField(max_length=64)
    adress = models.CharField(max_length=200)
    telephone = models.CharField(max_length=10)
    tel2 = models.CharField(max_length=10)
    email = models.CharField(max_length=120,default="none")

