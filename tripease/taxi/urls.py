from django.urls import path

from .views import taxi_user_register, taxi, register_taxi, book_taxi

app_name = 'taxi'

urlpatterns = [
    path('', taxi, name="taxi"),
    path('taxi_user_register/', taxi_user_register, name="taxi-user-register"),
    path('register_taxi/', register_taxi, name="register-taxi"),
    path('book_taxi/<int:taxi_id>/', book_taxi, name="book-taxi"),
]