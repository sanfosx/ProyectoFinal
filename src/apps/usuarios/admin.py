from django.contrib import admin

from .models import Usuario 


class UsuariosAdmin(admin.ModelAdmin):
	list_display = ['id', 'nombre','apellido', 'domicilio']


admin.site.register(Usuario, UsuariosAdmin)