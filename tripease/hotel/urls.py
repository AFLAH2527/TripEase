from django.urls import path

from .views import hotel_user_register, hotel, register_hotel, add_rooms, update_room, book_room

app_name = 'hotel'

urlpatterns = [
    path('', hotel, name="hotel"),
    path('hotel_user_register/', hotel_user_register, name="hotel-user-register"),
    path('register_hotel/', register_hotel, name="register-hotel"),
    path('add_rooms/<int:id>/', add_rooms, name="add-rooms"),
    path('update_room/<int:id>/', update_room, name="update-room"),
    path('book_room/<int:room_id>/', book_room, name="book-room"),
    
]