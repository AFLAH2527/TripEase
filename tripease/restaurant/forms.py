from django.forms import ModelForm

from .models import Restaurant

class RestaurantRegistrationForm(ModelForm):
    
    class Meta:
        model = Restaurant
        fields = "__all__"