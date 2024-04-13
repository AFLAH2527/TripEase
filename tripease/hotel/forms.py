from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Hotel, Room, RoomBooking


class HotelUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(HotelUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class HotelRegistrationForm(ModelForm):
    
    class Meta:
        model = Hotel
        fields = "__all__"


class AddRoomsForm(ModelForm):

    class Meta:
        model = Room
        fields = "__all__"