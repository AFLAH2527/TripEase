from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Restaurant, Item, Combo


class RestaurantUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RestaurantUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class RestaurantRegistrationForm(ModelForm):
    
    class Meta:
        model = Restaurant
        fields = "__all__"


class AddMenuItemForm(ModelForm):
    
    class Meta:
        model = Item
        fields = "__all__"


class AddMenuComboForm(ModelForm):
    
    class Meta:
        model = Combo
        fields = "__all__"