from django.shortcuts import render, get_object_or_404
import stripe_keys
from django.http import JsonResponse
from .models import Item

import stripe

stripe.api_key = stripe_keys.STRIPE_SECRET_KEY

def ItemView(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item.html', {'item':item, 'pk':pk})

def BuyView(request, pk):
    item = get_object_or_404(Item, pk=pk)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': item.price_id,
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )

    return JsonResponse({
        'session_id' : session.id,
        'stripe_public_key' : stripe_keys.STRIPE_PUBLIC_KEY
    })
