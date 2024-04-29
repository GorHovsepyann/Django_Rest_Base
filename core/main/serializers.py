from rest_framework import serializers
from .models import Car,Category

class CategorySerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Category
        fields = '__all__'

class CarSerializers(serializers.ModelSerializer):
    
    class Meta:
        
        model = Car
        fields = '__all__'