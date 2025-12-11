from django.urls import path
from . import views

urlpatterns = [
    path('confirm/', views.order_confirm, name='order_confirm'),
]