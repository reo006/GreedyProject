from rest_framework import viewsets

from apps.orders.models import Order
from apps.restaurants.models import Restaurant
from .serializers import OrderSerializer, RestaurantSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

