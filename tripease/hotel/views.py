from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from tripease.decorators import allowed_users

from .models import Hotel, Type

from .forms import HotelRegistrationForm


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
