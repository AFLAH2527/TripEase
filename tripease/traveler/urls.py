from django.urls import path

from .views import traveler_register, traveler, traveler_loyalty, generate_itinerary

app_name = 'traveler'

urlpatterns = [
    path('', traveler, name="traveler"),
    path('traveler_register/', traveler_register, name="traveler-register"),
    path('loyalty/', traveler_loyalty, name="traveler-loyalty"),
    path('generate_itinerary/', generate_itinerary, name="generate-itinerary")  
]