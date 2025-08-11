from django.urls import path
from pages.views import home_page_view, contact_pages_view, checkout_view, about_page_view, none_page_view, \
 wishlist_view

app_name = 'pages'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('contact/', contact_pages_view, name='contact'),
    path('checkout/', checkout_view, name='checkout'),
    path('about/', about_page_view, name='about'),
    path('page_not_found/', none_page_view, name='404'),
    path('wishlist', wishlist_view, name='wishlist'),
]
