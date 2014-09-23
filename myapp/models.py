from django.db import models

# Create your models here.

class Clothes(models.Model):
    mark = models.TextField()
    price = models.IntegerField()
