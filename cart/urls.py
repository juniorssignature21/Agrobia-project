# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.cart_summary, name='cart_summary'),
#     path('add/', views.cart_add, name='cart_add'),
#     path('delete/', views.cart_delete, name='cart_delete'),
#     path('update/', views.cart_update, name='cart_update'),
# ]

# cart/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('null_cart/', views.null_cart, name='null-cart'),
    path('update_cart_quantity/<int:product_id>/<str:action>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('decrease_cart_quantity/<int:product_id>/', views.decrease_cart_quantity, name='decrease_cart_quantity'),
    path('increase_cart_quantity/<int:product_id>/', views.increase_cart_quantity, name='increase_cart_quantity'),
]
