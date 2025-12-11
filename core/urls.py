from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),  # 追加
    path('menu/<str:item_name>/', views.menu_detail, name='menu_detail'),
    path('delivery/cancel/', views.cancel_delivery, name='cancel_delivery'),
    path("cart/", views.cart_view, name="cart"),
    path("cart/increase/<int:item_id>/", views.cart_increase, name="cart_increase"),
    path("cart/decrease/<int:item_id>/", views.cart_decrease, name="cart_decrease"),
    path("cart/delete/<int:item_id>/", views.cart_delete, name="cart_delete"),
    path("cart/add/<str:item_id>/", views.add_to_cart, name="add_to_cart"),
    path('delivery/restore/', views.restore_delivery, name='restore_delivery'),
    path("purchase/", views.purchase, name="purchase"),
    path('purchase/', views.purchase_view, name='purchase'),
    path('purchase/complete/', views.purchase_complete, name='purchase_complete'),
]

