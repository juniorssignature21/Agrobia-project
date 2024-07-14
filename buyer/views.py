# from rest_framework import generics
# from .models import Order, Cart, CartItem, MyInfo
# from .serializers import OrderSerializer, CartSerializer, CartItemSerializer
# from rest_framework import generics, status
# from rest_framework.response import Response
# from django.contrib.auth.models import User
# from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import BuyerSignupSerializer, BuyerLoginSerializer
# from django.contrib.auth import authenticate
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from vendor.models import Product
# from django.shortcuts import render, redirect
# from .models import Order

# class CartDetailView(generics.RetrieveAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = CartSerializer

#     def get_object(self):
#         cart, created = Cart.objects.get_or_create(buyer=self.request.user)
#         return cart

# class AddToCartView(generics.GenericAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = CartItemSerializer

#     def post(self, request, *args, **kwargs):
#         product_id = request.data.get('product_id')
#         quantity = request.data.get('quantity', 1)

#         try:
#             product = Product.objects.get(id=product_id)
#         except Product.DoesNotExist:
#             return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

#         cart, created = Cart.objects.get_or_create(buyer=request.user)

#         cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
#         if not created:
#             cart_item.quantity += int(quantity)
#         else:
#             cart_item.quantity = int(quantity)
#         cart_item.save()

#         return Response({'message': 'Product added to cart'}, status=status.HTTP_200_OK)


# class BuyerSignupView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = BuyerSignupSerializer

# class BuyerLoginView(generics.GenericAPIView):
#     serializer_class = BuyerLoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         refresh = RefreshToken.for_user(user)
#         return Response({
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         })


# class OrderListCreate(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

# class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
       