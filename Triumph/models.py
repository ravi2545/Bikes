from django.db import models


class Triumphbike(models.Model):
    modelname = models.CharField(max_length=20)
    year = models.IntegerField()
    price = models.IntegerField()
