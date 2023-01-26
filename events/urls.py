from events.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'events', EventViewSet)
urlpatterns = router.urls