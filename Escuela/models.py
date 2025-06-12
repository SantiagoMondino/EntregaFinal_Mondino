from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from .models import Profesor, Estudiante, Curso  
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='posts/')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=100, choices=[
        ('EDUCACION', 'Educación'),
        ('TECNOLOGIA', 'Tecnología'),
        ('CIENCIA', 'Ciencia'),
        ('OTROS', 'Otros')
    ])
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['-fecha_publicacion']

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comentario de {self.autor} en {self.post}"  

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    especialidad = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
   

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    matricula = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.matricula})"

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    codigo = models.CharField(max_length=10, unique=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    estudiantes = models.ManyToManyField(Estudiante, blank=True)
    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
    

