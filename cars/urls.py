from rest_framework.routers import DefaultRouter
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'cars', CarViewSet)
urlpatterns = router.urls