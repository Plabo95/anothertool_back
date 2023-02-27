from rest_framework.routers import DefaultRouter
from orders.views import OrderViewSet,  OrderStatsViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'order-stats', OrderStatsViewSet, basename='order-stats')

urlpatterns = router.urls
