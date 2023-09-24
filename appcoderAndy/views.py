from django.shortcuts import render, redirect
from .models import Curso
from django.http import HttpResponse
from .forms import cursosForm, EstudianteForm

def curso(req, nombre, camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    return HttpResponse(f"<p>Curso: {curso.nombre} - Camada: {curso.camada} ha sido creado con éxito!</p>")

def listar_cursos(req):
    lista = Curso.objects.all()
    return render(req, "lista_cursos.html", {"lista_cursos": lista})

def crear_curso(request):
    if request.method == 'POST':
        form = cursosForm(request.POST)
        if form.is_valid():
            curso = form.save()
            return redirect('crear_curso')  
    else:
        form = cursosForm()
    return render(request, 'crear_curso.html', {'form': form})

def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            estudiante = form.save()
            return redirect('crear_estudiante')  
    else:
        form = EstudianteForm()
    return render(request, 'crear_estudiante.html', {'form': form})
