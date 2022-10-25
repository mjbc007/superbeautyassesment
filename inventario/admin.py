from django import forms
from django import forms
from django.contrib import admin
from .models import Equipo, EquipoUsuario

class EquipoAdmin(admin.ModelAdmin):
    list_display = ['id', 'referencia', 'marca', 'tipo']
    list_filter = ('tipo',)
    search_fields = ['referencia',]

class EquipoUsuarioForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        lista_equipos = EquipoUsuario.objects.all().values_list('equipo__id', flat=True)
        self.fields['equipo'].queryset = Equipo.objects.all().exclude(pk__in=lista_equipos)

class EquipoUsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'equipo', 'usuario', 'fecha_asignacion']
    list_filter = ('fecha_asignacion', 'usuario')
    form = EquipoUsuarioForm

admin.site.register(Equipo, EquipoAdmin)
admin.site.register(EquipoUsuario, EquipoUsuarioAdmin)