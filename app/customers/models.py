from django.db import models
from phone_field import PhoneField

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    address = models.CharField()
    email = models.EmailField()
    phone = PhoneField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name