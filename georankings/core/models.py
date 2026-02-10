from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
  name = models.CharField(max_length=100)


def __str__(self):
  return self.name


class Rating(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  country = models.ForeignKey(Country, on_delete=models.CASCADE)
  score = models.IntegerField()


class Meta:
  unique_together = ('user', 'country')


class BlogPost(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  content = models.TextField()
  created = models.DateTimeField(auto_now_add=True)


def __str__(self):
  return self.title