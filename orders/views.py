# orders/views.py
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from catalog.models import Product  # Убедитесь, что Product используется вместо Item
from .models import Order

def index(request):
    return HttpResponse("Welcome to the Orders page!")

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/my_orders.html', {'orders': orders})

@login_required
def add_to_cart(request, item_id):
    product = get_object_or_404(Product, id=item_id)  # Убедитесь, что используется Product
    order, created = Order.objects.get_or_create(user=request.user, product=product, defaults={'quantity': 1})

    if not created:
        order.quantity += 1
        order.save()
    return redirect('orders:my_orders')





