from rest_framework import serializers
from .models import Doctor, Patient, Hospital

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'name', 'phone_number', 'specialist','geolocation','hospital')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'name', 'phone_number', 'alternate_phone_number', 'disease', 'geolocation', 'doctor')


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('id', 'name', 'phone_number', 'famous_for','geolocation')