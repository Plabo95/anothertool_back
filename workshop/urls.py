from rest_framework.routers import DefaultRouter
from workshop.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'workshop', WorkshopViewset)
urlpatterns = router.urls
