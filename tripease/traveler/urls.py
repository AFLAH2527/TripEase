from django.urls import path

from .views import traveler_register, traveler

app_name = 'traveler'

urlpatterns = [
    path('', traveler, name="traveler"),
    path('traveler_register/', traveler_register, name="traveler-register")    
]