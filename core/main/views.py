from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CarSerializers,CategorySerializers
from .models import Car,Category

class CategoryView(viewsets.ModelViewSet):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CarView(viewsets.ModelViewSet):
    
    queryset = Car.objects.all()
    serializer_class = CarSerializers