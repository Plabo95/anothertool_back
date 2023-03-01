from rest_framework import generics
from user.serializers import UserSerializer, MyTokenObtainPairSerializer

from rest_framework_simplejwt.views import TokenObtainPairView


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
