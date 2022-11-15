from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('phone_number', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        ("permissions", {"fields": ("is_active", "is_admin", "last_login")})
    )
    add_fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
    )
    filter_horizontal = ()
    ordering = ()


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
