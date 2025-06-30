from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='Principal'),  
    path('cursos/', views.cursos, name='Formulario'),
    path('contacto/', views.contacto, name='Contacto'),
]
