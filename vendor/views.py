# from rest_framework import generics
# from .models import Product, ProductCategory
# from .serializers import ProductSerializer
# from rest_framework import generics, status
# from rest_framework.response import Response
# from django.contrib.auth.models import User
# from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import VendorSignupSerializer, VendorLoginSerializer
# from django.contrib.auth import authenticate
# from rest_framework.permissions import AllowAny, IsAuthenticated

    
    
# class VendorSignupView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = VendorSignupSerializer

# class VendorLoginView(generics.GenericAPIView):
#     serializer_class = VendorLoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         refresh = RefreshToken.for_user(user)
#         return Response({
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         })


# class ProductListCreate(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(vendor=self.request.user)

# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated]

