from rest_framework.routers import DefaultRouter

from .views import OrderViewSet, RestaurantViewSet

router = DefaultRouter()
router.register('restaurants', RestaurantViewSet, basename='restaurant')
router.register('orders', OrderViewSet, basename='order')

urlpatterns = router.urls

