from invoices.models import *
from invoices.serializers import *

# RF
from rest_framework import permissions
from rest_framework import viewsets


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
