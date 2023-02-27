from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer,TestingSerializer
from .models import Product,Testing
# Create your views here.

class ProductListView(generics.ListCreateAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    
class TestingListView(generics.ListCreateAPIView):
    serializer_class=TestingSerializer
    queryset=Testing.objects.all()
    
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    
class TestingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=TestingSerializer
    queryset=Testing.objects.all()