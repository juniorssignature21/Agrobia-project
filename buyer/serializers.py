# from rest_framework import serializers
# from .models import Order, Cart, CartItem
# from rest_framework import serializers
# from django.contrib.auth.models import User
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth import authenticate


# class CartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = ['id', 'product', 'quantity']

# class CartSerializer(serializers.ModelSerializer):
#     items = CartItemSerializer(many=True, read_only=True)

#     class Meta:
#         model = Cart
#         fields = ['id', 'buyer', 'items']


# class BuyerSignupSerializer(serializers.ModelSerializer):
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
#         validated_data.pop('confirm_password')
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         return user

# class BuyerLoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Incorrect Credentials")


# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = '__all__'
