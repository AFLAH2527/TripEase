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
    destination = forms.ModelChoiceField(queryset=Destination.objects.all(), label="Destination", required=True)
    from_date = forms.DateField(label="From Date", widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    to_date = forms.DateField(label="To Date", widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    budget = forms.IntegerField(label="Budget (Total)", min_value=0, required=True)
    hotel_percentage = forms.IntegerField(label="Hotel Percentage", min_value=0, max_value=100, required=True)
    restaurant_percentage = forms.IntegerField(label="Restaurant Percentage", min_value=0, max_value=100, required=True)
    taxi_percentage = forms.IntegerField(label="Taxi Percentage", min_value=0, max_value=100, required=True)

    def clean(self):
        cleaned_data = super().clean()
        hotel_percentage = cleaned_data.get("hotel_percentage")
        restaurant_percentage = cleaned_data.get("restaurant_percentage")
        taxi_percentage = cleaned_data.get("taxi_percentage")

        total_percentage = hotel_percentage + restaurant_percentage + taxi_percentage
        if total_percentage != 100:
            self.add_error(None, "The total percentage must be 100.")

        return cleaned_data

    def clean_to_date(self):
        from_date = self.cleaned_data.get("from_date")
        to_date = self.cleaned_data.get("to_date")

        if from_date and to_date:
            duration = (to_date - from_date).days + 1
            if duration < 1:
                raise forms.ValidationError("The 'to date' must be after the 'from date'.")
            self.cleaned_data['duration'] = duration

        return to_date
