from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login

from tripease.decorators import allowed_users

from .models import Restaurant, Type, Combo, Item

from .forms import RestaurantUserCreationForm, RestaurantRegistrationForm, AddMenuItemForm, AddMenuComboForm

def restaurant_user_register(request):
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
        'form': form,
        'name': "Restaurant"
    }
    return render(request, 'registration/user_register.html', context)


@login_required
@allowed_users(allowed_roles = ['admin', 'restaurant'])
def restaurant(request):
    try:
        restaurant = Restaurant.objects.get(poc_name=request.user.username)
        combos = Combo.objects.filter(restaurant_name=restaurant.name)
        context = {
            'restaurant':restaurant,
            'combos': combos
        }
        return render(request, 'restaurant/restaurant.html', context)
    except:
        #Admin Login
        context = {
            'restaurant':"Admin",
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
                restaurant = Restaurant.objects.get(poc_name=user.username)
                form = RestaurantRegistrationForm(request.POST, instance=restaurant)
            except:
                form = RestaurantRegistrationForm(request.POST)

            if form.is_valid():
                form.save()
            return redirect('redirect-login')
        
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
    

@login_required
@allowed_users(allowed_roles = ['admin', 'restaurant'])
def add_menu_item(request):
    user = request.user
    try:
        if request.method == 'POST':
            form = AddMenuItemForm(request.POST)
            # try:
            #     restaurant = Restaurant.objects.get(poc_name=user.username)
            #     form = AddMenuItemsForm(request.POST, instance=restaurant)
            # except:
            #     form = AddMenuItemsForm(request.POST)

            if form.is_valid():
                form.save()
            return redirect('restaurant:restaurant')
        
        restaurant = Restaurant.objects.get(poc_name=user.username)
        context = {
            'restaurant':restaurant,
            # 'button':"Update"
        }
        return render(request, 'restaurant/add_menu_item.html', context)
        
    except:
        context = {
            # 'button':"Register"
        }
        return render(request, 'restaurant/add_menu_item.html', context)
    

@login_required
@allowed_users(allowed_roles = ['admin', 'restaurant'])
def add_menu_combo(request):
    user = request.user
    try:
        if request.method == 'POST':
            form = AddMenuComboForm(request.POST)
            # try:
            #     restaurant = Restaurant.objects.get(poc_name=user.username)
            #     form = AddMenuItemsForm(request.POST, instance=restaurant)
            # except:
            #     form = AddMenuItemsForm(request.POST)

            if form.is_valid():
                form.save()
            return redirect('restaurant:restaurant')
        
        restaurant = Restaurant.objects.get(poc_name=user.username)
        items = Item.objects.filter(restaurant_name=restaurant.name)
        context = {
            'restaurant':restaurant,
            'items': items            # 'button':"Update"
        }
        return render(request, 'restaurant/add_menu_combo.html', context)
        
    except:
        context = {
            # 'button':"Register"
        }
        return render(request, 'restaurant/add_menu_combo.html', context)




