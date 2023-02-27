from django.urls import path,include
from .views import ProductListView,TestingListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('testing',TestingListView,basename='testing')
router.register('products',ProductListView,basename='products')

urlpatterns = [
    path('',include(router.urls))
]