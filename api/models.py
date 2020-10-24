from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Hospital(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=100)
    famous_for = models.CharField(max_length=50)
    geolocation = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=100)
    specialist = models.CharField(max_length=50)
    geolocation = models.CharField(max_length=80)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    phone_number = PhoneNumberField()
    alternate_phone_number = PhoneNumberField()
    email = models.EmailField(max_length=100)
    disease = models.CharField(max_length=50)
    geolocation = models.CharField(max_length=80)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
