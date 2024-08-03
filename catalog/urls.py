# catalog/urls.py

from django.urls import path
from . import views

app_name = 'catalog'  # Пространство имен для приложения catalog

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница каталога
    # Удалены маршруты для отсутствующих представлений item_detail и category_list
]


