from django.shortcuts import render , redirect
from .models import Estudiante , Profesor, Curso
from .forms import ProfesorForm, EstudianteForm, CursoForm, BuscarEstudianteForm

def index(request):
    return render(request, 'index.html')

def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfesorForm()
    return render(request, 'agregar_profesor.html', {'form': form})

def listar_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesores_listar.html', {'profesores': profesores})

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EstudianteForm()
    return render(request, 'agregar_estudiante.html', {'form': form})

def listar_alumnos(request):
    alumnos = Estudiante.objects.all()
    return render(request, 'alumnos_listar.html', {'alumnos': alumnos})


def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CursoForm()
    return render(request, 'agregar_curso.html', {'form': form})

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'listar_curso.html', {'cursos': cursos})

def buscar_estudiante(request):
    estudiantes = None
    matricula_buscada = None
    
    if request.method == 'POST':
        form = BuscarEstudianteForm(request.POST)
        if form.is_valid():
            matricula_buscada = form.cleaned_data['matricula']
            estudiantes = Estudiante.objects.filter(matricula__icontains=matricula_buscada)
    else:
        form = BuscarEstudianteForm()
    
    return render(request, 'buscar_estudiante.html', {
        'form': form,
        'estudiantes': estudiantes,
        'matricula_buscada': matricula_buscada
    })
# Create your views here.
