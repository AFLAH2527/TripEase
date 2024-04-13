from django.urls import path

from .views import traveler_register, traveler, traveler_loyalty

app_name = 'traveler'

urlpatterns = [
    path('', traveler, name="traveler"),
    path('traveler_register/', traveler_register, name="traveler-register"),
    path('loyalty/', traveler_loyalty, name="traveler-loyalty")  
]