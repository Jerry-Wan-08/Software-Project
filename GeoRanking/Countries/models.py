from django.db import models

class Country(models.Model):
  name = models.CharField(max_length=255, default="Unknown")
  capital = models.CharField(max_length=255, default="Unknown")
  currency = models.CharField(max_length=100, default="USD")
  safety_index = models.FloatField(default="0")
  