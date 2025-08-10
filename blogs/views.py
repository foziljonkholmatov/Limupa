from django.shortcuts import render, get_object_or_404
from blogs.models import BlogModel

def blog_list(request):
    posts = BlogModel.objects.all().order_by('-created_at')
    return render(request, 'pages/blogs.html', {'posts': posts})


def blogs_details(request, pk):
    post = get_object_or_404(BlogModel, pk=pk)
    return render(request, 'pages/blog-details.html', {'post': post})
