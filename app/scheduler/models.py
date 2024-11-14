from django.db import models

from customers.models import Customer


# Create your models here.

class Event(models.Model):
    title = models.CharField()
    start = models.CharField()
    end = models.CharField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    numAnimals = models.IntegerField()
