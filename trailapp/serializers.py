from .models import Product,Testing
from rest_framework import serializers

class TestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testing
        fields = '__all__'
        
class ProductSerializer(serializers.ModelSerializer):
    testing=TestingSerializer(many=True,read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        