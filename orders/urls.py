# orders/urls.py
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.index, name='index'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
]


