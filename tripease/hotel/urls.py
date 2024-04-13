from django.urls import path

from .views import hotel_user_register, hotel, register_hotel, add_rooms

app_name = 'hotel'

urlpatterns = [
    path('', hotel, name="hotel"),
    path('hotel_user_register/', hotel_user_register, name="hotel-user-register"),
    path('register_hotel/', register_hotel, name="register-hotel"),
    path('add_rooms/', add_rooms, name="add-rooms")
    
]