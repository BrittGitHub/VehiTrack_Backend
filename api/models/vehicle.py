from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Vehicle(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  v_year = models.CharField(max_length=4)
  v_make = models.CharField(max_length=100)
  v_model = models.CharField(max_length=100)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"Hi, year:'{self.v_year}' make:{self.v_make} model:{self.v_model}."

  def as_dict(self):
    """Returns dictionary version of Vehicle models"""
    return {
        'id': self.id,
        'v_year': self.v_year,
        'v_make': self.v_make,
        'v_model': self.v_model
    }
