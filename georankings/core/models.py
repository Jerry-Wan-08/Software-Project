from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
  name = models.CharField(max_length=100, unique=True)

  safety_index = models.DecimalField(
      max_digits=5,
      decimal_places=2,
      help_text="Safety index out of 100"
  )

  cost_index = models.DecimalField(
      max_digits=5,
      decimal_places=2,
      help_text="Cost of living index (higher = more expensive)"
  )

  travel_rating = models.DecimalField(
      max_digits=3,
      decimal_places=1,
      help_text="Overall travel rating out of 10"
  )

  def __str__(self):
      return self.name
    
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