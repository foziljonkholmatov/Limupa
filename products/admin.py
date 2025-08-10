from django.contrib import admin
from .models import ProductModel


@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_new', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'reference')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
