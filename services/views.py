#rest fw
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView, Response
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from services.serializers import ServiceSerializer
from services.models import *

from rest_framework import viewsets



class ServiceViewSet(viewsets.ModelViewSet):
    #list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy()
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    #permission_classes = [permissions.IsAuthenticated]

# Create your views here.
@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def services(request,pk):
    services = Service.objects.filter(user=pk)
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)

@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def createService(request):
    serializer = ServiceSerializer(data=request.data)
    print(serializer.initial_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def updateService(request, pk, sk):
    service = Service.objects.get(user=pk, id = sk)
    serializer = ServiceSerializer(instance= service, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
#@permission_classes([IsAuthenticated])
def deleteService(request, pk, sk):
    service = Service.objects.get(user=pk, id = sk)
    service.delete()
    return Response()
