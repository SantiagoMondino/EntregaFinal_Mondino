from django import forms
from django.contrib.auth.forms import (
    UserCreationForm, 
    UserChangeForm,
    PasswordChangeForm
)
from django.utils.translation import gettext_lazy as _
from .models import Usuario

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label=_('Correo electrónico'),
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': _('ejemplo@dominio.com')
        }),
        required=True
    )
    first_name = forms.CharField(
        label=_('Nombre'),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Tu nombre')
        }),
        required=True
    )
    last_name = forms.CharField(
        label=_('Apellido'),
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Tu apellido')
        }),
        required=True
    )

    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Nombre de usuario')
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

class ProfileUpdateForm(UserChangeForm):
    password = None  
    
    fecha_nacimiento = forms.DateField(
        label=_('Fecha de nacimiento'),
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'},
            format='%Y-%m-%d'
        ),
        required=False
    )
    
    bio = forms.CharField(
        label=_('Biografía'),
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': _('Cuéntanos algo sobre ti...')
        }),
        required=False
    )

    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'avatar', 'fecha_nacimiento', 'bio')
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Nombre')
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Apellido')
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _('Correo electrónico')
            }),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'new-password'
            })