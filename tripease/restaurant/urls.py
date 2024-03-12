from django.urls import path

from .views import restaurant, register_restaurant

app_name = 'restaurant'

urlpatterns = [
    path('', restaurant, name="restaurant"),
    path('register_restaurant/', register_restaurant, name="register-restaurant")
]