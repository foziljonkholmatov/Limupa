
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from basket.cart import Basket
from products.models import ProductModel


def basket_detail(request):
    """
    Display the basket contents.
    """
    basket = Basket(request)
    return render(request, 'shop/shopping-cart.html', {'basket': basket})


def basket_add(request, product_id):
    """
    Add a product to the basket.
    """
    basket = Basket(request)
    product = get_object_or_404(ProductModel, id=product_id)

    basket.add(product=product, quantity=1)
    messages.success(request, f'{product.name} added to your basket!')
    return redirect('shop:product')

from django.http import HttpResponse

@require_POST
def basket_remove(request, product_id):
    print("basket_remove chaqirildi!", product_id, request.method)
    return HttpResponse("OK")


# Create your views here.
