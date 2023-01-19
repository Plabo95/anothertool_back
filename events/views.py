from django.shortcuts import render
from models import *

from rest_framework.decorators import api_view, permission_classes


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def events(request, pk):
    events = Event.objects.filter(user=pk).order_by('-start')
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def nextEvents(request, pk):
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())

    events = Event.objects.filter(user=pk, start__range=(today_start, today_end)).order_by('start')
    serializer = NextEventSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createEvent(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteEvent(request, pk, sk):
    event = Event.objects.get(user=pk, id=sk)
    client_id = event.client.id
    event.delete()
    sinpa = Event.objects.filter(user=pk, client=client_id, paid=False).count()      #Busco si tiene mas citas sin pagar
    if sinpa<1:
        Client.objects.filter(user=pk, id=client_id).update(moroso=False)
    return Response()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateEvent(request, pk, sk):
    event = Event.objects.get(user=pk, id=sk)
    serializer = EventSerializer(instance= event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
