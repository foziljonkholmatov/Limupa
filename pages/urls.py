from django.urls import path
from pages.views import home_page_view, contact_pages_view, checkout_view, about_page_view, none_page_view, \
    product_details_view, add_cart, wishlist_view, shop_list_view, blogs_view
from user.views import login_page, register_view, logout_page

app_name = 'pages'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('contact/', contact_pages_view, name='contact'),
    path('login/', login_page, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_page, name='logout',),
    path('checkout/', checkout_view, name='checkout'),
    path('about/', about_page_view, name='about'),
    path('page_not_found/', none_page_view, name='404'),
    path('product', product_details_view, name='product'),
    path('cart', add_cart, name='cart'),
    path('wishlist', wishlist_view, name='wishlist'),
    path('shop/', shop_list_view, name='shop'),
    path('blog', blogs_view, name='blog'),
]
