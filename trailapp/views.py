from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer,TestingSerializer
from .models import Product,Testing
from rest_framework.permissions import IsAuthenticated,BasePermission,IsAdminUser
# Create your views here.

class Check(BasePermission):
    def has_permission(self, request, view):
        user=request.user
        if request.method == 'GET':
            return True 
        elif request.method in ['POST','DELETE','PUT']:
            if user.is_superuser:
                return True
        return False

class ProductListView(ModelViewSet):
    permission_classes=[Check]
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    
class TestingListView(ModelViewSet):
    permission_classes=[Check]
    queryset=Testing.objects.all()
    serializer_class=TestingSerializer
    
# class ProductListView(generics.ListCreateAPIView):
#     serializer_class=ProductSerializer
#     queryset=Product.objects.all()
    
# class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class=ProductSerializer
#     queryset=Product.objects.all()
    
# class TestingListView(generics.ListCreateAPIView):
#     serializer_class=TestingSerializer
#     queryset=Testing.objects.all()
    
# class TestingDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class=TestingSerializer
#     queryset=Testing.objects.all()    