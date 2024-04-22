from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from hotel.models import Hotel
from restaurant.models import Restaurant
from taxi.models import Taxi


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
                return render(request, 'redirect_login.html')
        except:
            return HttpResponse("No hotels registered under this user")
    
    elif user_type=='restaurant':
        try:
            restaurant = Restaurant.objects.get(poc_name=user, email=user.email)
            if restaurant.admin_approved==True:
                return redirect('restaurant:restaurant')
            else:
                return render(request, 'redirect_login.html')
        except:
            return render(request, 'invalid_login.html')
    
    elif user_type=='taxi':
        try:
            taxi = Taxi.objects.get(poc_name=user, email=user.email)
            if taxi.admin_approved==True:
                return redirect('taxi:taxi')
            else:
                return render(request, 'redirect_login.html')
        except:
            return HttpResponse("No taxis registered under this user")
    
    elif user_type=='traveler':
        return redirect('traveler:traveler')

    else:
        return render(request, 'invalid_login.html')


def landing_page(request):
    return render(request, 'landing_page.html')