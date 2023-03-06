from rest_framework.routers import DefaultRouter
from invoices.views import InvoiceViewSet, InvoiceItemViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet, basename='invoices')
router.register(r'invoice-item', InvoiceItemViewSet, basename='invoice-item')
urlpatterns = router.urls
