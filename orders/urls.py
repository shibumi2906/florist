# orders/urls.py

from django.urls import path
from . import views

app_name = 'orders'  # Добавьте эту строку для задания пространства имен

urlpatterns = [
    path('', views.index, name='index'),
    # Другие маршруты...
]
