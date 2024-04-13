from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login

from tripease.decorators import allowed_users

from .models import Traveler

from .forms import TravelerUserCreationForm, TravelPlanForm


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
    if request.method == 'POST':
        form = TravelPlanForm(request.POST)
        if form.is_valid():
            destination = form.cleaned_data['destination']
            budget = form.cleaned_data['budget']
            duration = form.cleaned_data['duration']
            # Generate the itinerary based on user input (logic here)
            #itinerary = generate_itinerary(destination, budget, duration)
            # Render the itinerary to the user
            print(destination)
            print(budget)
            print(duration)
            return render(request, 'traveler/itinerary.html')
    else:
        form = TravelPlanForm()
        context = {
            'form':form
        }
    return render(request, 'traveler/traveler.html', context)


@login_required
@allowed_users(allowed_roles = ['admin', 'traveler'])
def traveler_loyalty(request):
    return render(request, 'traveler/traveler_loyalty.html')




