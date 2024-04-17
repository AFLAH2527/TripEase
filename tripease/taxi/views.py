from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login

from datetime import datetime, timedelta

from tripease.decorators import allowed_users

from .models import Taxi, Type, TaxiBooking
from loyalty.models import LoyaltyCard, LoyalPoint

from .forms import TaxiUserCreationForm, TaxiRegistrationForm


def taxi_user_register(request):
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
        'form': form,
        'name': "Taxi"
    }
    return render(request, 'registration/user_register.html', context)


@login_required
@allowed_users(allowed_roles = ['admin', 'taxi'])
def taxi(request):
    try:
        taxi = Taxi.objects.get(poc_name=request.user.username)
        context = {
            'taxi':taxi,
        }
        return render(request, 'taxi/taxi.html', context)
    except:
        #Admin Login
        context = {
            'taxi':"Admin",
        }
        return render(request, 'taxi/taxi.html', context)
    


@login_required
@allowed_users(allowed_roles = ['admin', 'taxi'])
def register_taxi(request):
    user = request.user
    types = Type.objects.all()
    try:
        if request.method == 'POST':
            try:
                hotel = Taxi.objects.get(poc_name=user.username)
                form = TaxiRegistrationForm(request.POST, instance=hotel)
            except:
                form = TaxiRegistrationForm(request.POST)

            if form.is_valid():
                form.save()
            return redirect('redirect-login')
        
        taxi = Taxi.objects.get(poc_name=user.username)
        context = {
            'user':user,
            'taxi':taxi,
            'button':"Update"
        }
        return render(request, 'taxi/register_taxi.html', context)
        
    except:
        context = {
            'user':user,
            'types':types,
            'button':"Register"
        }
        return render(request, 'taxi/register_taxi.html', context)
    

def book_taxi(request, taxi_id):
    taxi = Taxi.objects.get(pk=taxi_id)
    traveler_name = request.user.username
    loyal_points = LoyalPoint.objects.filter(traveler=request.user.username).first()
    loyalty_card = LoyaltyCard.objects.filter(card_holder=request.user.username).first()
    
    if request.method == 'POST':
        pickup_location = request.POST.get('pickup_location')
        destination = request.POST.get('destination')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        start_date = datetime.strptime(request.POST.get('start_date'), '%Y-%m-%d')
        end_date = datetime.strptime(request.POST.get('end_date'), '%Y-%m-%d')
        duration = end_date - start_date + timedelta(days=1)
        redeem_points = request.POST.get('redeem_points')
        discount = loyalty_card.card.multiple_factor * int(redeem_points)
        total_rent = taxi.daily_rent * duration.days

        loyal_points.points_redeemed += int(redeem_points)
        loyal_points.points_remain -= int(redeem_points)
        loyal_points.save()

        taxi_booking = TaxiBooking.objects.create(
            taxi=taxi,
            traveler_name=traveler_name,
            pickup_location=pickup_location,
            destination=destination,
            start_date=start_date,
            end_date=end_date,
            total_rent=total_rent - discount
        )

        # Set the available field of the corresponding Taxi to False
        taxi.available = False
        taxi.save()

        return redirect('traveler:generate-itinerary')  # Redirect to a success page after saving

    context = {
        'taxi_name': taxi.name,
        'traveler_name': traveler_name,
        'daily_rent': taxi.daily_rent
    }
    return render(request, 'taxi/book_taxi.html', context)




