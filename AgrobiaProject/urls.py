"""
URL configuration for AgrobiaProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/vendor/', include('vendor.urls')),
    # path('api/buyer/', include('buyer.urls')),
    path('vendor/', include('vendorapp.urls')),
    path('buyer/', include('buyerapp.urls')),
    path('cart/', include('cart.urls')),
    path('', include('store.urls')),
    path('vendor/api/', include('vendorapp.api.urls')),
    path('store/api/', include('store.api.urls')),
    path('cart/api/', include('cart.api.urls')),
    path('api/categories', include('categories.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)