from django.db import models

# Create your models here.

class persondetail(models.Model):
    Name=models.CharField(max_length=100)
    Phone=models.IntegerField()
    Address=models.CharField(max_length=200)
    Email=models.EmailField(max_length=30)