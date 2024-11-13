from django.db import models


class CuttingInstruction(models.Model):
    name = models.CharField()
    created = models.DateTimeField(auto_now_add=True)

# Create your models here.
class Primal(models.Model):
    name = models.CharField()
    cutting_instruction = models.ForeignKey(CuttingInstruction, related_name='primals', on_delete=models.CASCADE, null=True)

class Cut(models.Model):
    name = models.CharField()
    cutType = models.CharField()
    prepType = models.CharField()
    quantity = models.CharField()
    primal = models.ForeignKey(Primal, related_name='cuts', on_delete=models.CASCADE, null=True)

