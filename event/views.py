from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets


from .serializers import EventSerializer

from .models import Event


class EventView(viewsets.ModelViewSet):


	serializer_class = EventSerializer

	queryset = Event.objects.all()
