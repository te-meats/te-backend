from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField()
    start = models.CharField()
    end = models.CharField()
