# application urls

from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .import views

router = routers.DefaultRouter()
router.register('doctors', views.DoctorViewSet)
router.register('patients', views.PatientViewSet)
router.register('hospital', views.HospitalViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
