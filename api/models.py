from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=25)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=100)
    specialist = models.CharField(max_length=50)

    


