from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel


class CustomUserAdmin(UserAdmin):
    model = UserModel
    list_display = ('email', 'is_active', 'is_staff', 'created_at')
    search_fields = ('email',)
    ordering = ('-created_at',)

    readonly_fields = ('created_at', 'updated_at', 'last_login')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal data', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('System time', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
         ),
    )


admin.site.register(UserModel, CustomUserAdmin)

