from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from hotel.forms import HotelUserCreationForm
from restaurant.forms import RestaurantUserCreationForm
from taxi.forms import TaxiUserCreationForm

from hotel.models import Hotel
from restaurant.models import Restaurant
from taxi.models import Taxi


def hotel_register(request):
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
        'form': form
    }
    return render(request, 'registration/hotel_register.html', context)

def restaurant_register(request):
    if request.method == 'POST':
        form = RestaurantUserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            form = form.save()
            group = Group.objects.get(name="restaurant")
            form.groups.add(group)
            form.save()
            new_user = authenticate(username=username,
                                    password=password,
                                    )
            login(request, new_user)

        return redirect('restaurant:register-restaurant')
    
    form = RestaurantUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/restaurant_register.html', context)

def taxi_register(request):
    if request.method == 'POST':
        form = TaxiUserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            form = form.save()
            group = Group.objects.get(name="taxi")
            form.groups.add(group)
            form.save()
            new_user = authenticate(username=username,
                                    password=password,
                                    )
            login(request, new_user)

        return redirect('taxi:register-taxi')
    
    form = TaxiUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/taxi_register.html', context)


def redirect_login(request):
    user = request.user
    user_type = str(user.groups.all()[0])

    if user_type=='admin':
        return redirect('/admin/')

    elif user_type=='hotel':
        try:
            hotel = Hotel.objects.get(poc_name=user, email=user.email)
            if hotel.admin_approved==True:
                return redirect('hotel:hotel')
            else:
                return HttpResponse("Admin approvel pending")
        except:
            return HttpResponse("Invalid Login")
    
    elif user_type=='restaurant':
        try:
            restaurant = Restaurant.objects.get(poc_name=user, email=user.email)
            if restaurant.admin_approved==True:
                return redirect('restaurant:restaurant')
            else:
                return HttpResponse("Admin approvel pending")
        except:
            return HttpResponse("Invalid Login")
    
    elif user_type=='taxi':
        try:
            taxi = Taxi.objects.get(poc_name=user, email=user.email)
            if taxi.admin_approved==True:
                return redirect('taxi:taxi')
            else:
                return HttpResponse("Admin approvel pending")
        except:
            return HttpResponse("Invalid Login")
    
    else:
        return HttpResponse("Invalid Login")


def landing_page(request):
    return render(request, 'landing_page.html')