from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

User = get_user_model()

class Mensaje(models.Model):
    remitente = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='mensajes_enviados',
        verbose_name=_('remitente')
    )
    destinatario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='mensajes_recibidos',
        verbose_name=_('destinatario')
    )
    asunto = models.CharField(
        _('asunto'),
        max_length=200
    )
    contenido = models.TextField(
        _('contenido')
    )
    fecha_envio = models.DateTimeField(
        _('fecha de envío'),
        default=timezone.now
    )
    leido = models.BooleanField(
        _('leído'),
        default=False
    )
    
    class Meta:
        verbose_name = _('mensaje')
        verbose_name_plural = _('mensajes')
        ordering = ['-fecha_envio']
    
    def __str__(self):
        return f"{self.asunto} (De: {self.remitente}, Para: {self.destinatario})"
    
    def marcar_como_leido(self):
        if not self.leido:
            self.leido = True
            self.save()
    
    @property
    def es_nuevo(self):
        return not self.leido