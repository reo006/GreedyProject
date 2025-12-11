from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('restaurants/', include('apps.restaurants.urls')),
    path('orders/', include('apps.orders.urls')),
    path('api/', include('apps.api.urls')),
]