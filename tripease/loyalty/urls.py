from django.urls import path

from .views import loyalty_dashboard

app_name = 'loyalty'

urlpatterns = [
    path('', loyalty_dashboard, name="loyalty-dashboard"),
]


