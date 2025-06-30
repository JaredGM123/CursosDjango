from django.shortcuts import render

def principal(request):
    return render(request, 'inicio.html')

def cursos(request):
    return render(request, 'cursos.html')

def contacto(request):
    return render(request, 'contacto.html')
