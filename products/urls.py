from django.urls import path

from products.views import product_list, product_detail

app_name = 'shop'

urlpatterns = [
    path('', product_list, name='product'),
    path('product-details/<int:pk>/', product_detail, name='product-details')
]
