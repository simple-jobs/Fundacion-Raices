from django.contrib import admin
from .models import Inicio,QuienesSomo,Contacto,Proyecto,Documento, Paz, Comunidade,Fortalecimiento,Modernizacion
from django.contrib.auth.models import Group

class InicioAdmin(admin.ModelAdmin):
	list_display = ('presentacion',)

class QuienesSomoAdmin(admin.ModelAdmin):
	list_display = ('quienes_somos','mision','vision','objetivos',)

class PazAdmin(admin.ModelAdmin):
	list_display = ('descripcion',)

class ComunidadesAdmin(admin.ModelAdmin):
	list_display = ('descripcion',)

class FortalecimientoAdmin(admin.ModelAdmin):
	list_display = ('descripcion',)

class ModernizacionAdmin(admin.ModelAdmin):
	list_display = ('descripcion',)

class ProyectoAdmin(admin.ModelAdmin):
	list_display=('nombre','descripcion','archivo',)
	list_filter = ('nombre','descripcion','archivo',)
	search_fields = ('nombre', 'descripcion',)

class DocumentoAdmin(admin.ModelAdmin):
	list_display=('nombre','archivo',)
	list_filter = ('nombre','archivo',)
	search_fields = ('nombre',)
	


admin.site.unregister(Group)
admin.site.register(Inicio,InicioAdmin)
admin.site.register(QuienesSomo,QuienesSomoAdmin)
admin.site.register(Paz, PazAdmin)
admin.site.register(Comunidade, ComunidadesAdmin)
admin.site.register(Fortalecimiento, FortalecimientoAdmin)
admin.site.register(Modernizacion, FortalecimientoAdmin)
admin.site.register(Contacto)
admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(Documento,DocumentoAdmin)