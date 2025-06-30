from django.db import models

class Curso(models.Model):
    titulo = models.CharField('Título', max_length=150)
    descripcion = models.TextField('Descripción')
    nivel = models.IntegerField('Nivel')
    activo = models.BooleanField('Activo', default=True)
    fecha_inicio = models.DateField('Fecha de inicio', null=True, blank=True)
    duracion = models.DurationField('Duración', null=True, blank=True)
    imagen = models.ImageField('Imagen', upload_to='cursos/')
    fecha_creacion = models.DateTimeField('Fecha de creación', auto_now_add=True)

    def __str__(self):
        return self.titulo
