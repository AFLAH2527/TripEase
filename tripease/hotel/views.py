from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login

from tripease.decorators import allowed_users

from .models import Hotel, Type

from .forms import HotelRegistrationForm, HotelUserCreationForm


def hotel_user_register(request):
    if request.method == 'POST':
        form = HotelUserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            form = form.save()
            group = Group.objects.get(name="hotel")
            form.groups.add(group)
            form.save()
            new_user = authenticate(username=username,
                                    password=password,
                                    )
            login(request, new_user)

        return redirect('hotel:register-hotel')
    
    form = HotelUserCreationForm()
    context = {
        'form': form,
        'name': "Hotel"
    }
    return render(request, 'registration/user_register.html', context)

@login_required
@allowed_users(allowed_roles = ['admin', 'hotel'])
def hotel(request):
    hotels = Hotel.objects.all()
    context = {
        'hotels':hotels
    }
    return render(request, 'hotel/hotel.html', context)


@login_required
@allowed_users(allowed_roles = ['admin', 'hotel'])
def register_hotel(request):
    user = request.user
    types = Type.objects.all()
    try:
        if request.method == 'POST':
            try:
                hotel = Hotel.objects.get(poc_name=user.username)
                form = HotelRegistrationForm(request.POST, instance=hotel)
            except:
                form = HotelRegistrationForm(request.POST)

            if form.is_valid():
                form.save()
            return redirect('hotel:hotel')
        
        hotel = Hotel.objects.get(poc_name=user.username)
        context = {
            'user':user,
            'hotel':hotel,
            'types':types,
            'button':"Update"
        }
        return render(request, 'hotel/register_hotel.html', context)
        
    except:
        context = {
            'user':user,
            'types':types,
            'button':"Register"
        }
        return render(request, 'hotel/register_hotel.html', context)
