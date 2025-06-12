from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
from django.utils.translation import gettext_lazy as _

class Usuario(AbstractUser):
  
    bio = models.TextField(
        _('biografía'),
        blank=True,
        null=True,
        help_text=_('Cuéntanos algo sobre ti')
    )
    fecha_nacimiento = models.DateField(
        _('fecha de nacimiento'),
        blank=True,
        null=True
    )
    avatar = ResizedImageField(
        _('avatar'),
        size=[300, 300],
        crop=['middle', 'center'],
        quality=90,
        upload_to='avatars/',
        blank=True,
        null=True,
        help_text=_('Imagen cuadrada de al menos 300x300 px')
    )
    
    
    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')
        ordering = ['-date_joined']
    
    
    def __str__(self):
        return self.get_full_name() or self.username
    
    @property
    def nombre_completo(self):
        return self.get_full_name()
    
    @property
    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        return '/static/images/default-avatar.png'