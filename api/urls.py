# application urlss
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .import views

app_name = "api"

router = routers.DefaultRouter()
router.register('doctors', views.DoctorViewSet)
router.register('patients', views.PatientViewSet)
router.register('hospital', views.HospitalViewSet)


urlpatterns = [
    path("", views.home , name='home'),
    path("/api/", include(router.urls)),
]
