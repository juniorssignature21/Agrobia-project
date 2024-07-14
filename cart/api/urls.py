# cart/api/urls.py
from django.urls import path
from cart.api.views import CartItemListCreateView, CartItemDetailView

urlpatterns = [
    path('cart-items/', CartItemListCreateView.as_view(), name='cartitem-list-create'),
    path('cart-items/<int:pk>/', CartItemDetailView.as_view(), name='cartitem-detail'),
]
