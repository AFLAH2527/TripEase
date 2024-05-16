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
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView
from .views import landing_page, redirect_login

urlpatterns = [
    path('', landing_page, name='landing-page'),
    path('register/type', TemplateView.as_view(template_name='registration/select_account_type.html'), name='register-type'),
    path('admin/', admin.site.urls),
    path('hotel/', include('hotel.urls', namespace='hotel')),
    path('restaurant/', include('restaurant.urls', namespace='restaurant')),
    path('taxi/', include('taxi.urls', namespace='taxi')),
    path('traveler/', include('traveler.urls', namespace='traveler')),
    path('loyalty/', include('loyalty.urls', namespace='loyalty')),
    path('auth/', include(urls)),
    path('redirect_login/', redirect_login, name='redirect-login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
