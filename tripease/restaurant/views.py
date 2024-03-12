from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from tripease.decorators import allowed_users

from .models import Restaurant, Type

from .forms import RestaurantRegistrationForm


@login_required
@allowed_users(allowed_roles = ['admin', 'restaurant'])
def restaurant(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants':restaurants
    }
    return render(request, 'restaurant/restaurant.html', context)


@login_required
@allowed_users(allowed_roles = ['admin', 'restaurant'])
def register_restaurant(request):
    user = request.user
    types = Type.objects.all()
    try:
        if request.method == 'POST':
            try:
                hotel = Restaurant.objects.get(poc_name=user.username)
                form = RestaurantRegistrationForm(request.POST, instance=hotel)
            except:
                form = RestaurantRegistrationForm(request.POST)

            if form.is_valid():
                form.save()
            return redirect('restaurant:restaurant')
        
        restaurant = Restaurant.objects.get(poc_name=user.username)
        context = {
            'user':user,
            'restaurant':restaurant,
            'button':"Update"
        }
        return render(request, 'restaurant/register_restaurant.html', context)
        
    except:
        context = {
            'user':user,
            'types':types,
            'button':"Register"
        }
        return render(request, 'restaurant/register_restaurant.html', context)
