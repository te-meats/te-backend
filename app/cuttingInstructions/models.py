from django.db import models

# Create your models here.
class PrepTypeList(models.Model):
    name = models.CharField()

class SecondaryPrepTypeList(models.Model):
    name = models.CharField()

class PrimalList(models.Model):
    name = models.CharField()

class CutList(models.Model):
    name = models.CharField()

class PrepType(models.Model):
    name = models.CharField()

class SecondaryPrepType(models.Model):
    name = models.CharField()

class CutType(models.Model):
    name = models.CharField()

class Cut(models.Model):
    name = models.CharField()
    cutType = models.CharField()
    prepType = models.CharField()
    secondaryPrepType = models.CharField()
    unit = models.CharField()

class Primal(models.Model):
    name = models.CharField()
    cuts = models.ManyToManyField(Cut)

class CuttingInstructions(models.Model):
    name = models.CharField()
    bodyParts = models.ManyToManyField(Primal)   
    created = models.DateTimeField(auto_now_add=True)
