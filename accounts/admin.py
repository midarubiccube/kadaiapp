from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserChangeForm, AdminUserCreationForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
                                                )
    add_fieldsets = ((None, {'classes': ('wide',), 'fields': ('username', 'email', 'department', 'password1', 'password2'), }),)
    form = CustomUserChangeForm
    add_form = AdminUserCreationForm
    list_display = ('username', 'email', 'department', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)