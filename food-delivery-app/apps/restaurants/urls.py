from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='restaurant_search'),
    path('cart/', views.cart, name='cart'),
]