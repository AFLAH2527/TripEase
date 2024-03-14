"""
URL configuration for tripease project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import urls
from django.contrib import admin
from django.urls import path, include

from .views import landing_page, hotel_register, restaurant_register, taxi_register, redirect_login

urlpatterns = [
    path('', landing_page, name='landing-page'),
    path('admin/', admin.site.urls),
    path('hotel/', include('hotel.urls', namespace='hotel')),
    path('restaurant/', include('restaurant.urls', namespace='restaurant')),
    path('taxi/', include('taxi.urls', namespace='taxi')),
    path('auth/register/hotel/', hotel_register, name='hotel-register'),
    path('auth/register/restaurant/', restaurant_register, name='restaurant-register'),
    path('auth/register/taxi/', taxi_register, name='taxi-register'),
    path('auth/', include(urls)),
    path('redirect_login/', redirect_login, name='redirect-login'),
]
