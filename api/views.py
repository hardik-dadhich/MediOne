from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DoctorSerializer
from .models import Doctor

# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer