from django.db import models

# Create your models here.

<<<<<<< Updated upstream
class Clothes(models.Model):
    names=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    front_photo=models.ImageField(upload_to='itemphoto/',default=None)
    back_photo=models.ImageField(upload_to='itemphoto/',default=None)
    detail=models.TextField(default=None)
=======
class Shoes(models.Model):
    names = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='photo/', default=None)
    detail = models.TextField(default= None)
    star = models.ImageField(upload_to='photo/', default=None)
    discount = models.DecimalField( max_digits=5, decimal_places=2)
>>>>>>> Stashed changes
