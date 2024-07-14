from django.urls import path
from . import views

urlpatterns = [
    path('', views.vendorform, name='vendor-form'),
    # path('product_upload/', views.prod_upload, name='products-upload'),
    path('product_upload/', views.productsupload, name='products-upload'),
    path('product_page/', views.product_pages, name='products-pages'),
    path('sell-on-agrobia/', views.check_vendor_status, name='check-vendor-status'),
    path('activities/', views.activity, name='activities'),
]
