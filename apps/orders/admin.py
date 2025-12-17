from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'restaurant_name', 'total_price', 'status', 'order_date')
    list_filter = ('status', 'restaurant_name')
    search_fields = ('user__username', 'restaurant_name')

