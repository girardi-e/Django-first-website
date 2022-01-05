from django.db import models


# Product model and attributes
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


# Offer model and attributes
class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
