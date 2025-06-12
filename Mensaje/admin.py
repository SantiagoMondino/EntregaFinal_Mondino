from django.contrib import admin
from .models import Mensaje
from django.utils.translation import gettext_lazy as _

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ('asunto', 'remitente', 'destinatario', 'fecha_envio', 'leido')
    list_filter = ('leido', 'fecha_envio', 'remitente', 'destinatario')
    search_fields = ('asunto', 'contenido', 'remitente__username', 'destinatario__username')
    date_hierarchy = 'fecha_envio'
    ordering = ('-fecha_envio',)
    
    fieldsets = (
        (None, {
            'fields': ('remitente', 'destinatario', 'asunto', 'contenido')
        }),
        (_('Metadata'), {
            'fields': ('fecha_envio', 'leido'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('fecha_envio',)

# Register your models here.
