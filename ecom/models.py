from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=250)
    price = models.FloatField()
    img = models.CharField(max_length=255)
    descr = models.TextField()
    