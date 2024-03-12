from django.urls import path

from .views import taxi, register_taxi

app_name = 'taxi'

urlpatterns = [
    path('', taxi, name="taxi"),
    path('register_taxi/', register_taxi, name="register-taxi")
]