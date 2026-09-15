from django.db import models

# Create your models here.

class Hat(models.Model):
    names = models.CharField(max_length=100,default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='hat')
    more  = models.TextField(default=None)
    
class more(models.Model):
    names=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='mr_Hat/',default=None)
    orders=models.IntegerField()