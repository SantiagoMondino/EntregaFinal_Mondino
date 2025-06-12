from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Usuario
from .forms import ProfileUpdateForm

class UsuarioAdmin(UserAdmin):
    form = ProfileUpdateForm
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('-date_joined',)
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Información Personal'), {
            'fields': (
                'first_name', 
                'last_name', 
                'email', 
                'avatar',
                'fecha_nacimiento',
                'bio'
            )
        }),
        (_('Permisos'), {
            'fields': (
                'is_active', 
                'is_staff', 
                'is_superuser',
                'groups', 
                'user_permissions'
            ),
        }),
        (_('Fechas importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 
                'email',
                'first_name',
                'last_name',
                'password1', 
                'password2'
            ),
        }),
    )

admin.site.register(Usuario, UsuarioAdmin)

