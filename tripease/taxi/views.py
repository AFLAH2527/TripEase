from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login

from tripease.decorators import allowed_users

from .models import Taxi, Type

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
    taxis = Taxi.objects.all()
    context = {
        'taxis':taxis
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
            return redirect('taxi:taxi')
        
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
