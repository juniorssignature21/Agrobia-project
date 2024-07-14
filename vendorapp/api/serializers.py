# vendor/api/serializers.py
from rest_framework import serializers
from vendor.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
