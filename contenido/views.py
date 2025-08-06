from django.shortcuts import render
from .models import Curso

def principal(request):
    return render(request, 'inicio.html')

def cursos(request):
    return render(request, 'cursos.html')

def contacto(request):
    return render(request, 'contacto.html')

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'contenido/cursos.html', {'cursos': cursos})