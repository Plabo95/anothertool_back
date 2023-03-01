from clients.models import *
from clients.serializers import *

# RF
from rest_framework import permissions
from rest_framework import viewsets


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Client.objects.filter(
            user=self.request.user).order_by('-created_at')
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
