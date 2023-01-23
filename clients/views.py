from clients.models import *
from clients.serializers import *

#RF
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView, Response
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def clients(request, pk):
    clients = Client.objects.filter(user=pk)
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)

@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def createClient(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def updateClient(request, pk, sk):
    client = Client.objects.get(user=pk, id = sk)
    serializer = ClientSerializer(instance= client, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
#@permission_classes([IsAuthenticated])
def deleteClient(request, pk, sk):
    client = Client.objects.get(user=pk, id = sk)
    client.delete()
    return Response()