# store/api/urls.py
from django.urls import path
from store.api.views import RegisterUserView, LoginView

urlpatterns = [
    path('api-register/', RegisterUserView.as_view(), name='api-register'),
    path('api-login/', LoginView.as_view(), name='api-login'),
]
