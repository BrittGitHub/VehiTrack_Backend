from django.db import models
from django.contrib.auth import get_user_model
from .vehicle import Vehicle

# Create your models here.


class Maintenance(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  type = models.CharField(max_length=100)
  date = models.DateField()
  cost = models.DecimalField(max_digits=11, decimal_places=2)
  notes = models.CharField(max_length=100)
  # Creating a field called `vehicle`
  # this field is going to be a foreign key, meaning that this entry will be a primary key from our vehicle model
  # on_delete=models.CASCADE - is when we delete a vehicle delete their maintenances
  vehicle = models.ForeignKey(
      Vehicle, on_delete=models.CASCADE, related_name='maintenances')

  # owner = models.ForeignKey(
  #     get_user_model(),
  #     on_delete=models.CASCADE
  # )

  def __str__(self):
    # This must return a string
    return f"Type:'{self.type}' date:{self.date} model:{self.cost} notes:{self.notes}."

  # def as_dict(self):
  #   """Returns dictionary version of Maintenance models"""
  #   return {
  #       'id': self.id,
  #       'type': self.type,
  #       'date': self.date,
  #       'cost': self.cost,
  #       'notes': self.string
  #   }
