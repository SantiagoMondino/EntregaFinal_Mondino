from django import forms
from django.contrib.auth import get_user_model
from .models import Mensaje
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class MensajeForm(forms.ModelForm):
    destinatario = forms.ModelChoiceField(
        label=_('Destinatario'),
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    asunto = forms.CharField(
        label=_('Asunto'),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Asunto del mensaje')
        })
    )
    contenido = forms.CharField(
        label=_('Contenido'),
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': _('Escribe tu mensaje aquí...')
        })
    )

    class Meta:
        model = Mensaje
        fields = ['destinatario', 'asunto', 'contenido']
    
    def __init__(self, *args, **kwargs):
        self.remitente = kwargs.pop('remitente', None)
        super().__init__(*args, **kwargs)
        
        
        if self.remitente:
            self.fields['destinatario'].queryset = User.objects.exclude(id=self.remitente.id)
    
    def save(self, commit=True):
        mensaje = super().save(commit=False)
        mensaje.remitente = self.remitente
        if commit:
            mensaje.save()
        return mensaje