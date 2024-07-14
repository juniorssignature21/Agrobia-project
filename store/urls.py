from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name="home"),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
    path('user-profile/', views.user_details, name='user-profile'),
    path('', views.product_section, name='home'),
]
