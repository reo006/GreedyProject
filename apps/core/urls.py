from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('menu/<str:item_name>/', views.menu_detail, name='menu_detail'),
    path('delivery/cancel/', views.cancel_delivery, name='cancel_delivery'),
    path('delivery/restore/', views.restore_delivery, name='restore_delivery'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<str:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/increase/<int:item_id>/', views.cart_increase, name='cart_increase'),
    path('cart/decrease/<int:item_id>/', views.cart_decrease, name='cart_decrease'),
    path('cart/delete/<int:item_id>/', views.cart_delete, name='cart_delete'),
    path('cart/update/<int:item_id>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('cart/remove/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('purchase/', views.purchase, name='purchase'),
    path('purchase/complete/', views.purchase_complete, name='purchase_complete'),
]

