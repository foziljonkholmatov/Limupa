from django.contrib import messages
from django.shortcuts import render, redirect
from pages.forms import ContactModelForm


def none_page_view(request):
    return render(request, 'pages/404.html')


def home_page_view(request):
    return render(request, 'home.html')


def checkout_view(request):
    return render(request, 'pages/checkout.html')


def about_page_view(request):
    return render(request, 'pages/about-us.html')



def add_cart(request):
    return render(request, 'shop/shopping-cart.html')


def wishlist_view(request):
    return render(request, 'pages/wishlist.html')


def shopping_cart_view(request):
    return render(request, 'shop/shopping-cart.html')


def contact_pages_view(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your contact has been sent to admins!'
            )
            return redirect('pages:contact')
        else:
            messages.error(
                request, 'Please correct your data!'
            )
    else:
        form = ContactModelForm()
    return render(request, 'pages/contact.html', {'form': form})
