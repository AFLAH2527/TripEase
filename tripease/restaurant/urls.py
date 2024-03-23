from django.urls import path

from .views import restaurant_user_register, restaurant, register_restaurant, add_menu_item, add_menu_combo

app_name = 'restaurant'

urlpatterns = [
    path('', restaurant, name="restaurant"),
    path('restaurant_user_register/', restaurant_user_register, name="restaurant-user-register"),
    path('register_restaurant/', register_restaurant, name="register-restaurant"),
    path('add_menu_item/', add_menu_item, name="add-menu-item"),
    path('add_menu_combo/', add_menu_combo, name="add-menu-combo"),
]