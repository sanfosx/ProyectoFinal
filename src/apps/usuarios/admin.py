from django.contrib import admin

from .models import Usuario 


class UsuariosAdmin(admin.ModelAdmin):
	list_display = ['id', 'username','first_name','last_name', 'email','comparte', 'ptos_totales']


admin.site.register(Usuario, UsuariosAdmin)