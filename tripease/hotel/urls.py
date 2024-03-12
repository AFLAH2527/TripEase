from django.urls import path

from .views import hotel, register_hotel

app_name = 'hotel'

urlpatterns = [
    path('', hotel, name="hotel"),
    path('register_hotel/', register_hotel, name="register-hotel")
]