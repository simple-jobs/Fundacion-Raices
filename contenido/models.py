from django.db import models

class Inicio(models.Model):
	presentacion = models.TextField(max_length=700,verbose_name="Texto de Bienvenida",)

	def __unicode__(self):
		return 'Informacion de presentacion'



class QuienesSomo(models.Model):
	quienes_somos = models.TextField(max_length=700,verbose_name="Quienes Somos",)
	mision = models.TextField(max_length=700,verbose_name="Mision",)
	vision = models.TextField(max_length=700,verbose_name="Vision",)
	objetivos = models.TextField(max_length=700,verbose_name="Objetivos",)

	def __unicode__(self):
		return 'Quienes Somos'

class Contacto(models.Model):
	nombre = models.CharField(max_length=255,verbose_name="Nombre de contacto",)
	correo = models.CharField(max_length=255,verbose_name="Correo de contacto",)
	telefono1 = models.CharField(max_length=255,verbose_name="Telefono de contacto # 1",)
	telefono2 = models.CharField(max_length=255,verbose_name="Telefono de contacto # 1", blank=True, null=True,)
	facebook = models.CharField(max_length=255,verbose_name="Link de facebook",)
	twiter = models.CharField(max_length=255,verbose_name="Link de Twiter",)

	def __unicode__(self):
		return 'Datos de Contacto'

class Proyecto(models.Model):
	nombre = models.CharField(max_length=255,verbose_name="Nombre del proyecto",)
	descripcion = models.TextField(max_length=25000,verbose_name="Descripcion del proyecto",)

	def __unicode__(self):
		return self.nombre

class Documento(models.Model):
	nombre = models.CharField(max_length=255,verbose_name="Nombre del Documento",)
	archivo = models.FileField(upload_to='documentos/', blank=True, null=True,)

	def __unicode__(self):
		return 'Centro de Documentacion'


class Imagene(models.Model):
	nombre = models.CharField(max_length=255,verbose_name="Titulo de la imagen",)
	descripcion = models.CharField(max_length=255,verbose_name="Descripcion de la imagen",)
	imagen = models.ImageField(upload_to="imagenes/",verbose_name="Imagen para galeria" , blank=True, null=True)


	def __unicode__(self):
		return self.nombre



class Paz(models.Model):
	descripcion = models.TextField(max_length=1000,verbose_name="Paz, Seguridad y Postconflicto",)

class Comunidade(models.Model):
	descripcion = models.TextField(max_length=1000,verbose_name="Comunidades y Medio Ambiente Sostenible",)

class Fortalecimiento(models.Model):
	descripcion = models.TextField(max_length=1000,verbose_name="Fortalecimiento Institucional",)

class Modernizacion(models.Model):
	descripcion = models.TextField(max_length=1000,verbose_name="Modernizacion de Gobiernos Locales",)


