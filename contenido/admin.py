from django.contrib import admin
from .models import Inicio,QuienesSomo,Investigacione,Contacto,Proyecto,Documento
from django.contrib.auth.models import Group

class InicioAdmin(admin.ModelAdmin):
	list_display = ('presentacion',)

class QuienesSomoAdmin(admin.ModelAdmin):
	list_display = ('quienes_somos','mision','vision','objetivos',)

class InvestigacioneAdmin(admin.ModelAdmin):
	list_display=('presentacion','paz','comunidades','fortalecimiento','modernizacion',)

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
admin.site.register(Investigacione,InvestigacioneAdmin)
admin.site.register(Contacto)
admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(Documento,DocumentoAdmin)