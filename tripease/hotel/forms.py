from django.forms import ModelForm

from .models import Hotel

class HotelRegistrationForm(ModelForm):
    
    class Meta:
        model = Hotel
        fields = "__all__"