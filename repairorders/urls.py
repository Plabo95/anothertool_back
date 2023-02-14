from rest_framework.routers import DefaultRouter
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'repairorders', RepairOrderViewset)
urlpatterns = router.urls