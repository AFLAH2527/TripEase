from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login

from tripease.decorators import allowed_users

from .models import Traveler
from hotel.models import Hotel, Room, RoomBooking
from restaurant.models import Restaurant, Combo, ComboBooking
from taxi.models import Taxi, TaxiBooking
from loyalty.models import LoyalPoint, LoyaltyCard

from .forms import TravelerUserCreationForm, TravelPlanForm
from loyalty.forms import LoyaltyCardPurchaseForm



def generate_itinerary(request):
    destination = request.session.get('destination')
    budget = request.session.get('budget')
    duration = request.session.get('duration')
    hotel_percentage = request.session.get('hotel_percentage')
    restaurant_percentage = request.session.get('restaurant_percentage')
    taxi_percentage = request.session.get('taxi_percentage')

    # Hotel
    hotel_budget = hotel_percentage*(budget/100)
    room_budget = hotel_budget/duration

    hotels = Hotel.objects.filter(place=destination)
    rooms = Room.objects.filter(hotel_name__in=hotels, price__lte=room_budget, count__gt=0)
    
    print("Itinerary-----")
    print(room_budget)
    print(destination)
    print(hotels)
    print(rooms)

    # Restaurant
    restaurant_budget = restaurant_percentage*(budget/100)
    daily_restaurant_budget = restaurant_budget/duration
    onetime_restaurant_budget = daily_restaurant_budget/3

    restaurants = Restaurant.objects.filter(place=destination)
    combos = Combo.objects.filter(restaurant_name__in=restaurants, price__lte=onetime_restaurant_budget)

    print(onetime_restaurant_budget)
    print(destination)
    print(restaurants)
    print(combos)

    # Taxi
    taxi_budget = taxi_percentage*(budget/100)
    daily_taxi_budget = taxi_budget/duration

    taxis = Taxi.objects.filter(place=destination, daily_rent__lte=daily_taxi_budget, available=True)

    print(daily_taxi_budget)
    print(destination)
    print(taxis)

    context = {
        'destination': destination,
        'budget': budget,
        'duration': duration,
        'rooms': rooms,
        'combos': combos,
        'taxis': taxis
    }
    return render(request, 'traveler/itinerary.html', context)


def traveler_register(request):
    if request.method == 'POST':
        form = TravelerUserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            form = form.save()
            group = Group.objects.get(name="traveler")
            form.groups.add(group)
            form.save()
            new_user = authenticate(username=username,
                                    password=password,
                                    )
            login(request, new_user)

        return redirect('traveler:traveler')
    
    form = TravelerUserCreationForm()
    context = {
        'form': form,
        'name': "Traveler"
    }
    return render(request, 'registration/user_register.html', context)


@login_required
@allowed_users(allowed_roles = ['admin', 'traveler'])
def traveler(request):

    # Update current date of the Loyalty Card
    try:
        loyalty_card = LoyaltyCard.objects.get(card_holder=request.user.username, active=True)
        loyalty_card.current_date = timezone.now().date()
        loyalty_card.save()
    except:
        pass

    room_bookings = combo_bookings = taxi_bookings = None
    room_bookings_upcoming = room_bookings_completed = None

    if request.method == 'POST':
        travel_plan_form = TravelPlanForm(request.POST)
        if travel_plan_form.is_valid():
            request.session['destination'] = travel_plan_form.cleaned_data['destination'].name
            request.session['budget'] = travel_plan_form.cleaned_data['budget']
            request.session['duration'] = travel_plan_form.cleaned_data['duration']
            request.session['hotel_percentage'] = travel_plan_form.cleaned_data['hotel_percentage']
            request.session['restaurant_percentage'] = travel_plan_form.cleaned_data['restaurant_percentage']
            request.session['taxi_percentage'] = travel_plan_form.cleaned_data['taxi_percentage']
            # Generate the itinerary based on user input (logic here)
            return redirect('traveler:generate-itinerary')
            
    else:
        traveler_name = request.user.username
        room_bookings = RoomBooking.objects.filter(traveler_name=traveler_name)
        combo_bookings = ComboBooking.objects.filter(traveler_name=traveler_name)
        taxi_bookings = TaxiBooking.objects.filter(traveler_name=traveler_name)

        # Filter room bookings based on start and end dates
        current_date = timezone.now().date()
        room_bookings_upcoming = room_bookings.filter(start_date__gt=current_date)
        room_bookings_completed = room_bookings.filter(end_date__lte=current_date)

        # Separate upcoming and completed Combo Bookings
        upcoming_combo_bookings = combo_bookings.filter(food_date__gte=timezone.now().date())
        completed_combo_bookings = combo_bookings.filter(food_date__lt=timezone.now().date())
        
    loyal_points = LoyalPoint.objects.filter(traveler=request.user.username).first()

    context = {
            'travel_plan_form': TravelPlanForm(),
            'room_bookings': room_bookings,
            'room_bookings_upcoming': room_bookings_upcoming,
            'room_bookings_completed': room_bookings_completed,
            'combo_bookings': combo_bookings,
            'upcoming_combo_bookings': upcoming_combo_bookings,
            'completed_combo_bookings': completed_combo_bookings,
            'taxi_bookings': taxi_bookings,
            'loyal_points': loyal_points
    }
    return render(request, 'traveler/traveler.html', context)


@login_required
@allowed_users(allowed_roles = ['admin', 'traveler'])
def traveler_loyalty(request):
    return render(request, 'traveler/traveler_loyalty.html')




