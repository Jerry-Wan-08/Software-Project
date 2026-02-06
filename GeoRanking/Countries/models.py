from django.db import models

class Country(models.Model):
  name = models.CharField(max_length=255)
  capital = models.CharField(max_length=255)
  currency = models.CharField(max_length=100)
  safety_index = models.FloatField()
  