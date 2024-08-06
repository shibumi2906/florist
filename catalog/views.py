# catalog/views.py

from django.shortcuts import render, get_object_or_404
from .models import Item
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    items = Item.objects.all()
    return render(request, 'catalog/index.html', {'items': items})

def item_detail(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'catalog/item_detail.html', {'item': item})

def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    cart = request.session.get('cart', [])
    cart.append(item.id)
    request.session['cart'] = cart
    return HttpResponseRedirect(reverse('catalog:index'))

def my_orders(request):
    cart = request.session.get('cart', [])
    items = Item.objects.filter(id__in=cart)
    return render(request, 'orders/my_orders.html', {'items': items})
