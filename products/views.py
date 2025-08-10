from django.shortcuts import render, get_object_or_404
from .models import ProductModel

def product_list(request):
    products = ProductModel.objects.all().order_by('-created_at')
    return render(request, 'shop/shop.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    return render(request, 'shop/product-details.html', {'product': product})

