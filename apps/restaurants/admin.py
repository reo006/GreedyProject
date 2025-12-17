from django.contrib import admin
from .models import MenuItem, Restaurant

admin.site.register(Restaurant)
admin.site.register(MenuItem)

