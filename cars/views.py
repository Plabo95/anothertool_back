from .models import *
from .serializers import *

# RF
from rest_framework import permissions
from rest_framework import viewsets


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Car.objects.filter(
            user=self.request.user).order_by('-created_at')
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
