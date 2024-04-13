from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Destination, Traveler

class TravelerUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50)
    native_place = forms.CharField(max_length=50)
    district = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'name', 'phone', 'native_place', 'district', 'state')

    def save(self, commit=True):
        user = super(TravelerUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            # Now, save the associated Traveler object
            traveler = Traveler.objects.create(
                name=self.cleaned_data['name'],
                email=user.email,
                phone=self.cleaned_data['phone'],
                native_place=self.cleaned_data['native_place'],
                district=self.cleaned_data['district'],
                state=self.cleaned_data['state']
            )
        return user


class TravelPlanForm(forms.Form):
    destination = forms.ModelChoiceField(queryset=Destination.objects.all(),label="Destination", required=True)
    budget = forms.IntegerField(label="Budget (Total)", min_value=0, required=True)
    duration = forms.IntegerField(label="Trip Duration (Days)", min_value=1, required=True)
