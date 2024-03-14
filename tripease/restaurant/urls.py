from django.urls import path

from .views import restaurant_user_register, restaurant, register_restaurant

app_name = 'restaurant'

urlpatterns = [
    path('', restaurant, name="restaurant"),
    path('restaurant_user_register/', restaurant_user_register, name="restaurant-user-register"),
    path('register_restaurant/', register_restaurant, name="register-restaurant")
]