from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import CustomUser


@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    """
    Custom UserAdmin for the custom User model
    """

    list_display = (
        'id',
        'get_identifier',
        'first_name',
        'last_name',
        'is_active',
    )

    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
        'last_login',
    )

    search_fields = ('username', 'email', 'first_name', 'last_name')

    ordering = ('-date_joined',)

    filter_horizontal = ('groups', 'user_permissions')

    # Fieldsets for editing existing users
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        (_('Authentication Info'), {
            'fields': ('email',),
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {
            'fields': ('last_login',)
        }),
    )

    # Fieldsets for adding new users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff')
        }),
    )

    readonly_fields = ('last_login',)

    def get_identifier(self, obj):
        """
        Display the primary identifier (username, email, or phone)
        """
        if obj.username:
            return obj.username
        elif obj.email:
            return obj.email
        return "No identifier"

    get_identifier.short_description = 'Identifier'
