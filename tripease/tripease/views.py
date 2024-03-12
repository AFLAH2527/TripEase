from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def hotel_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
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
    
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/hotel_register.html', context)

def restaurant_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
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
    
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/restaurant_register.html', context)

def taxi_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
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
    
    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/taxi_register.html', context)


def landing_page(request):
    return render(request, 'landing_page.html')