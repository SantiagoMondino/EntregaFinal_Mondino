from django import forms
from .models import Profesor, Estudiante, Curso

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'
        widgets = {
            'fecha_incorporacion': forms.DateInput(attrs={'type': 'date'}),
        }

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

class BuscarEstudianteForm(forms.Form):
    matricula = forms.CharField(
        label='Número de Matrícula',
        max_length=10,
        required=True,
        help_text='Ingrese la matrícula completa o parcial del estudiante'
    )
