from django.urls import path
from pages.views import home_page_view, contact_pages_view, checkout_view
from user.views import login_page, register_view, logout_page

app_name = 'pages'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('contact/', contact_pages_view, name='contact'),
    path('login/', login_page, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_page, name='logout', ),
    path('checkout/', checkout_view, name='checkout'),
]
