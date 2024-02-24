from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CarSerializers
from .models import Car

# Create your views here.

class CarView(viewsets.ModelViewSet):
    
    queryset = Car.objects.all()
    serializer_class = CarSerializers