from django.contrib import admin
from .models import Cart, CartItem, Delivery  # 使ってるモデルに合わせて

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Delivery)



