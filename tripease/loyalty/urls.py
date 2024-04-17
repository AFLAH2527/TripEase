from django.urls import path

from .views import loyalty_dashboard, purchase_card, add_loyal_points

app_name = 'loyalty'

urlpatterns = [
    path('', loyalty_dashboard, name="loyalty-dashboard"),
    path('purchase_card/', purchase_card, name="purchase-card"),
    path('add_loyal_points/<int:card_points>/', add_loyal_points, name="add-loyal-points"),
]


