from unicodedata import category
from django.db import models

# create your model here:

class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    barcode = models.IntegerField(unique=True)

    