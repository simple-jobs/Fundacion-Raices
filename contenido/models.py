from django.db import models

class Inicio(models.Model):
	presentacion = models.TextField(max_length=700,verbose_name="Texto de Bienvenida",)

	class Meta:
		verbose_name = "Informacion del Inicio"
		verbose_name_plural = "Informacion del Inicio"

	def __unicode__(self):
		return 'Informacion de presentacion'



class QuienesSomo(models.Model):
	quienes_somos = models.TextField(max_length=700,verbose_name="Quienes Somos",)
	mision = models.TextField(max_length=700,verbose_name="Mision",)
	vision = models.TextField(max_length=700,verbose_name="Vision",)
	objetivos = models.TextField(max_length=700,verbose_name="Objetivos",)

	class Meta:
		verbose_name = "Informacion sobre nosotros"
		verbose_name_plural = "Informacion sobre nosotros"

	def __unicode__(self):
		return 'Quienes Somos'


class Proyecto(models.Model):
	nombre = models.CharField(max_length=255,verbose_name="Nombre del proyecto",)
	descripcion = models.TextField(max_length=40000000,verbose_name="Descripcion del proyecto",)

	class Meta:
		verbose_name = "Informacion de Proyecto"
		verbose_name_plural = "Informacion de Proyectos"

	def __unicode__(self):
		return self.nombre

class Documento(models.Model):
	nombre = models.CharField(max_length=255,verbose_name="Nombre del Documento",)
	archivo = models.FileField(upload_to='documentos/', blank=True, null=True,)

	class Meta:
		verbose_name = "Centro de documentos"
		verbose_name_plural = "Centro de documentacion"

	def __unicode__(self):
		return 'Centro de Documentacion'


class Imagene(models.Model):
	nombre = models.CharField(max_length=255,verbose_name="Titulo de la imagen",)
	descripcion =  models.TextField(max_length=1000,verbose_name="Descripcion de la imagen",)
	imagen = models.ImageField(upload_to="imagenes/",verbose_name="Imagen para galeria" , blank=True, null=True)

	class Meta:
		verbose_name = "Galelia de imagenes"
		verbose_name_plural = "Galeria de imagenes"

	def __unicode__(self):
		return self.nombre



class Paz(models.Model):
	descripcion = models.TextField(max_length=1000,verbose_name="Paz, Seguridad y Postconflicto",)

	class Meta:
		verbose_name = "Informacion sobre apartado Paz, Seguridad y Postconflicto"
		verbose_name_plural = "Informacion sobre apartado Paz, Seguridad y Postconflicto"

class Comunidade(models.Model):
	descripcion = models.TextField(max_length=1000,verbose_name="Comunidades y Medio Ambiente Sostenible",)

	class Meta:
		verbose_name = "Informacion sobre apartado Comunidades y Medio Ambiente Sostenible"
		verbose_name_plural = "Informacion sobre apartado Comunidades y Medio Ambiente Sostenible"




class Fortalecimiento(models.Model):
	descripcion = models.TextField(max_length=1000,verbose_name="Fortalecimiento Institucional",)

	class Meta:
		verbose_name = "Informacion sobre apartado Fortalecimiento Institucional"
		verbose_name_plural = "Informacion sobre apartado Fortalecimiento Institucional"

class Modernizacion(models.Model):
	descripcion = models.TextField(max_length=1000,verbose_name="Modernizacion de Gobiernos Locales",)

	class Meta:
		verbose_name = "Informacion sobre apartado Modernizacion de Gobiernos Locales"
		verbose_name_plural = "Informacion sobre apartado Modernizacion de Gobiernos Locales"


