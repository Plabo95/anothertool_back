from rest_framework.routers import DefaultRouter
from invoices.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
urlpatterns = router.urls
