from django.urls import path
from .views import ProductListView,TestingListView,ProductDetailView,TestingDetailView

urlpatterns = [
    path('products',ProductListView.as_view()),
    path('testing',TestingListView.as_view()),
    path('products/<int:pk>',ProductDetailView.as_view()),
    path('testing/<int:pk>',TestingDetailView.as_view()),
]