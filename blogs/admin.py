from django.contrib import admin

from blogs.models import BlogModel
from pages.templatetags.my_tags import register


@register.admin(BlogModel)

