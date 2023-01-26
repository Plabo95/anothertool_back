from events.models import *
from events.serializers import *
from clients.models import *

from datetime import datetime, timedelta, time

#rest fw
from rest_framework import permissions
from rest_framework import viewsets

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    #permission_classes = [permissions.IsAuthenticated]

 
#@permission_classes([IsAuthenticated])
def nextEvents(request, pk):
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())

    events = Event.objects.filter(user=pk, start__range=(today_start, today_end)).order_by('start')
    serializer = NextEventSerializer(events, many=True)
    return Response(serializer.data)
