from django import forms
from .models import LoyaltyCard, CardType

class LoyaltyCardPurchaseForm(forms.ModelForm):
    class Meta:
        model = LoyaltyCard
        fields = ['card', 'duration']
        
