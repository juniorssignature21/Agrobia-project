# store/api/views.py
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from store.api.serializers import UserSerializer

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token, created = Token.objects.get_or_create(user=response.data['id'])
        return Response({
            'token': token.key,
            'user_id': response.data['id'],
            'username': response.data['username']
        })


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token, created = Token.objects.get_or_create(user=response.data['id'])
        return Response({
            'token': token.key,
            'user_id': response.data['id'],
            'username': response.data['username']
        })
