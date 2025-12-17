from rest_framework import serializers

from apps.orders.models import Order
from apps.restaurants.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'phone_number', 'rating', 'cuisine_type']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'restaurant_name', 'items', 'total_price', 'order_date', 'status']

