# from rest_framework import serializers
# from .models import Product
# from categories.serializers import CategorySerializer
# from django.contrib.auth.models import User
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth import authenticate

# # class VendorSerializer(serializers.ModelSerializer):
# #     pass
# class VendorSignupSerializer(serializers.ModelSerializer):
    
#     confirm_password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ['username', 'password', 'confirm_password', 'email']
#         extra_kwargs = {'password': {'write_only': True}}

#     def validate(self, data):
#         if data['password'] != data['confirm_password']:
#             raise serializers.ValidationError("Passwords do not match")
#         return data

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password'],
#             # confirm_password=validated_data['confirm_password']
#         )
#         return user

# class VendorLoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Incorrect Credentials")

    

# class ProductSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()

#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'description', 'price', 'stock', 'category', 'vendor']
        

