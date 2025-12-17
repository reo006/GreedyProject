from django.contrib import admin
from .models import Cart, CartItem, Delivery, Imagemodel

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "canceled", "canceled_at")
    list_filter = ("canceled", "date")
    search_fields = ("user__username",)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user",)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity", "cart")
    list_filter = ("cart",)
    search_fields = ("name",)

@admin.register(Imagemodel)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id",)
