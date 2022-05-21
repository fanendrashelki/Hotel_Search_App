from email.headerregistry import Address
from django.db import models

# Create your models here.

class Emenities(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class hotel(models.Model):
    hotel_name=models.CharField(max_length=50)
    hotel_description=models.TextField(max_length=100)
    hotel_images=models.CharField(max_length=100)
    price=models.IntegerField()
    emenities=models.ManyToManyField(Emenities)

    def __str__(self):
        return self.hotel_name

