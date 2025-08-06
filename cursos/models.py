from django.db import models

class Curso(models.Model):
    NIVEL_CHOICES = [
        (1, 'Básico'),
        (2, 'Intermedio'),
        (3, 'Avanzado'),
    ]
    
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    nivel = models.IntegerField(choices=NIVEL_CHOICES, default=1)
    activo = models.BooleanField(default=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.titulo
    
    def get_nivel_display(self):
        return dict(self.NIVEL_CHOICES)[self.nivel]