from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DoctorSerializer, PatientSerializer, HospitalSerializer
from .models import Doctor, Patient, Hospital
from rest_framework.authentication import TokenAuthentication

# Create your views here.

def home(request):
    # request.session['is_login'] = True
    return render(request, "index.html", {})


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    authentication_classes = (TokenAuthentication, )


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    authentication_classes = (TokenAuthentication, )


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    authentication_classes = (TokenAuthentication, )

