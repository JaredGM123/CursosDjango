from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'get_nivel_display', 'fecha_inicio', 'activo', 'fecha_creacion')
    list_filter = ('nivel', 'activo', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion')
    date_hierarchy = 'fecha_creacion'
    ordering = ('-fecha_creacion',)
    fieldsets = (
        (_('Información Básica'), {
            'fields': ('titulo', 'descripcion', 'nivel', 'activo')
        }),
        (_('Fechas e Imagen'), {
            'fields': ('fecha_inicio', 'imagen')
        }),
    )
    
    def get_nivel_display(self, obj):
        return obj.get_nivel_display()
    get_nivel_display.short_description = _('Nivel')