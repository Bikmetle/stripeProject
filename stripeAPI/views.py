from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.urls import reverse
from .models import Item
import os
import stripe

PRICE_ID = "price_1McDEWGQ7a1wQCsd4MfEbpJp"

def index(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    session = stripe.checkout.Session.create(
        peyment_method_types=['card'],
        line_items=[{
            'price_data': PRICE_ID,
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('success')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request.build_absolute_uri(reverse('cancel')),
    )
    context = {
        'session_id': session.id,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    }
    return render(request, 'index.html')


def BuyView(request, buy_id):
    items = get_object_or_404(Item, pk=buy_id)
    return render(request, 'index.html', {'items':items})

def ItemView(request, item_id):
    items = get_object_or_404(Item, pk=item_id)
    return render(request, 'index.html', {'items':items})