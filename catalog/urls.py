# catalog/urls.py

from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('my_orders/', views.my_orders, name='my_orders'),
]

