from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from tripease.decorators import allowed_users

from .models import Taxi, Type

from .forms import TaxiRegistrationForm


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
