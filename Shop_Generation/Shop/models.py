from django.db import models

# Create your models here.

class Clothes(models.Model):
    names=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    front_photo=models.ImageField(upload_to='itemphoto/',default=None)
    back_photo=models.ImageField(upload_to='itemphoto/',default=None)
    detail=models.TextField(default=None)