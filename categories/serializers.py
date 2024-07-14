from rest_framework import serializers
from vendor.models import ProductCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'description']