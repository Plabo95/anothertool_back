from django.urls import path
from services.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
urlpatterns = router.urls


