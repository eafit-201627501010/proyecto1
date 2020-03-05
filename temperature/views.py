from django.shortcuts import render

from rest_framework import viewsets
from .models import temperature
from .serializers import temperatureSerializer

class ViewSet(viewsets.ModelViewSet):
    queryset = temperature.objects.all().order_by('-created')
    serializer_class = temperatureSerializer
