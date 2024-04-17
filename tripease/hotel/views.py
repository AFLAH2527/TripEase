from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login

from tripease.decorators import allowed_users

from .models import Hotel, Type, Room, RoomBooking
from loyalty.models import LoyalPoint, LoyaltyCard

from .forms import HotelRegistrationForm, HotelUserCreationForm, AddRoomsForm


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
    hotel = Hotel.objects.get(poc_name=request.user.username)
    rooms = Room.objects.filter(hotel_name=hotel.id)
    context = {
        'hotel':hotel,
        'rooms':rooms
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
            return redirect('redirect-login')
        
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


@login_required
@allowed_users(allowed_roles = ['admin', 'hotel'])
def add_rooms(request):
    user = request.user
    try:
        if request.method == 'POST':
            form = AddRoomsForm(request.POST)
            # try:
            #     restaurant = Restaurant.objects.get(poc_name=user.username)
            #     form = AddMenuItemsForm(request.POST, instance=restaurant)
            # except:
            #     form = AddMenuItemsForm(request.POST)

            if form.is_valid():
                form.save()
            return redirect('hotel:hotel')
        
        hotel = Hotel.objects.get(poc_name=user.username)
        context = {
            'hotel':hotel,
            # 'button':"Update"
        }
        return render(request, 'hotel/add_rooms.html', context)
        
    except:
        context = {
            # 'button':"Register"
        }
        return render(request, 'hotel/add_rooms.html', context)
    

@login_required
@allowed_users(allowed_roles = ['admin', 'hotel', 'traveler'])
def book_room(request, room_id):
    room = Room.objects.get(pk=room_id)
    traveler_name = request.user.username
    amount = room.price
    loyal_points = LoyalPoint.objects.filter(traveler=request.user.username).first()
    loyalty_card = LoyaltyCard.objects.filter(card_holder=request.user.username).first()

    if request.method == 'POST':
        # Retrieve data from POST request
        hotel_name = room.hotel_name
        no_of_days = request.POST.get('no_of_days')
        traveler_name = request.user.username
        redeem_points = request.POST.get('redeem_points')
        discount = loyalty_card.card.multiple_factor * int(redeem_points)
        amount = room.price * int(no_of_days)

        loyal_points.points_redeemed += int(redeem_points)
        loyal_points.points_remain -= int(redeem_points)
        loyal_points.save()

        # Create RoomBooking object and save to database
        room_booking = RoomBooking.objects.create(
            hotel_name=hotel_name,
            room=room,
            traveler_name=traveler_name,
            no_of_days=no_of_days,
            amount=amount-discount
        )
        # Redirect to a success page after saving
        return redirect('traveler:generate-itinerary')
    
    context = {
        'hotel_name': room.hotel_name.name,
        'room_type': room.room_type,
        'traveler_name': traveler_name,
        'amount': amount,
        'loyal_points': loyal_points
    }
    return render(request, 'hotel/book_room.html', context)