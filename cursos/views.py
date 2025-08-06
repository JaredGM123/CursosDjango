from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from .forms import CursoForm


def cursos(request):
    cursos = Curso.objects.all()
    print("Cursos desde la vista:", cursos) 
    return render(request, 'cursos/cursos.html', {'cursos': cursos})


def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos/formulario_curso.html', {'form': form})

def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/formulario_curso.html', {'form': form})

def eliminar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    curso.delete()
    return redirect('cursos')



def consultasSQL(request):
    alumnos = Alumnos.objects.raw(
        '''
        SELECT id, matricula, nombre, carrera, turno, imagen
        FROM registros_alumnos
        WHERE carrera = "TI"
        ORDER BY turno DESC
        '''
    )

    return render(request, "registros/consultas.html", {'alumnos': alumnos})

