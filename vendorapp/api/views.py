# vendor/api/views.py
from rest_framework import generics
from vendor.models import Product
from vendorapp.api.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user.farmer)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
