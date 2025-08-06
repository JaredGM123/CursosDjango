from django.shortcuts import render, redirect, get_object_or_404
from cursos.models import Curso
from cursos.forms import CursoForm  # asumo que el formulario está en cursos/forms.py

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'contenido/cursos.html', {'cursos': cursos})

def crear_curso(request):
    form = CursoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('cursos')
    return render(request, 'contenido/formulario_curso.html', {'form': form})

def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    form = CursoForm(request.POST or None, request.FILES or None, instance=curso)
    if form.is_valid():
        form.save()
        return redirect('cursos')
    return render(request, 'contenido/formulario_curso.html', {'form': form})

def eliminar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    curso.delete()
    return redirect('cursos')
