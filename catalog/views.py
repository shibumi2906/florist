# catalog/views.py

from django.shortcuts import render
from .models import Item

def index(request):
    items = Item.objects.all()  # Получаем все товары из базы данных
    return render(request, 'catalog/index.html', {'items': items})

def item_detail(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'catalog/item_detail.html', {'item': item})

