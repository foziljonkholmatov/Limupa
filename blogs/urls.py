from django.urls import path
from blogs.views import blog_list, blogs_details

app_name = 'blog'

urlpatterns = [
    path('', blog_list, name='blog'),
    path('blogs/<int:pk>/', blogs_details, name='blog-details'),

]
