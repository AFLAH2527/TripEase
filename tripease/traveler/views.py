from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login

from tripease.decorators import allowed_users

from .models import Traveler

from .forms import TravelerUserCreationForm


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
    travelers = Traveler.objects.all()
    context = {
        'travelers':travelers
    }
    return render(request, 'traveler/traveler.html', context)
