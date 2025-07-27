from django.contrib import messages
from django.shortcuts import render, redirect
from pages.forms import ContactModelForm


def home_page_view(request):
    return render(request, 'home.html')

def checkout_view(request):
    return render(request, 'pages/checkout.html')

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