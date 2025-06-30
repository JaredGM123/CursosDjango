from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'nivel', 'activo', 'fecha_inicio', 'fecha_creacion')
    ordering = ('fecha_creacion',)
    search_fields = ('titulo', 'descripcion')
    list_filter = ('activo', 'nivel', 'fecha_inicio')
    date_hierarchy = 'fecha_creacion'
