from django.contrib import admin
from .models import Equipo

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'color_camiseta', 'hinchada')

admin.site.register(Equipo, EquipoAdmin)
