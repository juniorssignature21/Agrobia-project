from django.shortcuts import render
from .serializers import CategorySerializer
from .models import ProductCategory
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status


# Create your views here.
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]