from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from tripease.decorators import allowed_users


@login_required
@allowed_users(allowed_roles = ['admin'])
def loyalty_dashboard(request):
    return render(request, 'loyalty/loyalty_dashboard.html')
