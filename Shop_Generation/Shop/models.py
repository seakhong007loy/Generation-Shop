from django.db import models
from django.contrib import admin
# Create your models here.
class Bags(models.Model):
    names= models.CharField(max_length=300)
    name_model= models.CharField(max_length=300)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='bags')
    photos = models.ImageField(upload_to='bags')
    photoback= models.ImageField(upload_to='bags')
    detail_bags=models.TextField(default=None)
