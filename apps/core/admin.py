from django.contrib import admin
from .models import Delivery


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'canceled', 'canceled_at')
    list_filter = ('canceled', 'date')
    search_fields = ('user__username',)

