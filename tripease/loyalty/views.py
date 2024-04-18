from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from tripease.decorators import allowed_users

from .forms import LoyaltyCardPurchaseForm
from .models import LoyaltyCard, CardType, LoyalPoint

@login_required
@allowed_users(allowed_roles = ['admin'])
def loyalty_dashboard(request):
    return render(request, 'loyalty/loyalty_dashboard.html')

@login_required
@allowed_users(allowed_roles = ['admin','traveler'])
def purchase_card(request):
    # Get available card types
    available_card_types = CardType.objects.all()

    try:
        loyalty_card = LoyaltyCard.objects.get(card_holder=request.user.username)
        if loyalty_card.active:
            context = {
                'active': "You already have an active card",
                'loyalty_card': loyalty_card
            }
            return render(request, 'loyalty/purchase_card.html', context)
        
    except:
        pass
    

    if request.method == 'POST':
        form = LoyaltyCardPurchaseForm(request.POST)
        if form.is_valid():
            # Process form data and create a new LoyaltyCard instance
            card_type = form.cleaned_data['card']
            duration = form.cleaned_data['duration']
            
            # Get the selected CardType object
            selected_card_type = CardType.objects.get(pk=card_type.pk)
            
            # Calculate total points based on card type and duration
            card_points = selected_card_type.points * duration
            
            # Create a new LoyaltyCard instance
            new_card = LoyaltyCard.objects.create(
                card=selected_card_type,
                card_holder=request.user.username,  # Set card holder as logged-in user
                duration=duration,
                total_points=card_points
            )
            
            # Redirect to a success page or any other appropriate view
            return redirect('loyalty:add-loyal-points', card_points)  # Replace 'loyalty:purchase-success' with the appropriate URL name
        
    else:
        form = LoyaltyCardPurchaseForm()

    context = {
        'form': form,
        'available_card_types': available_card_types
    }
    return render(request, 'loyalty/purchase_card.html', context)


def add_loyal_points(request, card_points):
    # Get the logged-in user's loyalty points instance if it exists, or create a new one
    loyal_point, created = LoyalPoint.objects.get_or_create(traveler=request.user.username, defaults={'card_points_purchased': 0})

    # Update the loyalty points based on the purchased card
    if created:
        # If a new instance was created, set initial values
        loyal_point.card_points_purchased = card_points
        loyal_point.earned_points = 0
        loyal_point.points_remain = card_points
        loyal_point.points_redeemed = 0
        loyal_point.total_points = card_points
    else:
        # If the user already has existing points, update them
        loyal_point.card_points_purchased += card_points
        loyal_point.points_remain += card_points
        loyal_point.total_points += card_points

    # Save the updated or newly created loyalty points instance
    loyal_point.save()

    # Redirect to a success page or any other appropriate view
    return redirect('traveler:traveler')  # Replace 'loyalty:update-points-success' with the appropriate URL name

    
        
