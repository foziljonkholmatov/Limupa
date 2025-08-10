from django.contrib import admin
from blogs.models import BlogModel
from pages.templatetags.my_tags import register


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'comments_count']
    search_fields = ['title', 'author']
    list_filter = ['updated_at']


