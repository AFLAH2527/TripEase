from django.forms import ModelForm

from .models import Taxi

class TaxiRegistrationForm(ModelForm):
    
    class Meta:
        model = Taxi
        fields = "__all__"