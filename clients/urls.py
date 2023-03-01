from rest_framework.routers import DefaultRouter
from clients.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='clients')
urlpatterns = router.urls
