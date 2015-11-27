from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View
from .models import Inicio, QuienesSomo, Contacto, Proyecto, Documento, Paz, Comunidade, Fortalecimiento, Modernizacion


class HomeView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['data'] = Inicio.objects.all().last()
		return context

class AboutView(TemplateView):
	template_name = 'about.html'
	def get_context_data(self, **kwargs):
		context = super(AboutView, self).get_context_data(**kwargs)
		context['quienes_somos'] =  QuienesSomo.objects.all().last()
		return context

class PeaceView(TemplateView):
	template_name = 'paz.html'
	def get_context_data(self, **kwargs):
		context = super(PeaceView, self).get_context_data(**kwargs)
		context['paz'] =  Paz.objects.all().last()
		return context

class CommunityView(TemplateView):
	template_name = 'comunidades.html'
	def get_context_data(self, **kwargs):
		context = super(CommunityView, self).get_context_data(**kwargs)
		context['comunidades'] =  Comunidade.objects.all().last()
		return context

class StrengtheningView(TemplateView):
	template_name = 'fortalecimiento.html'
	def get_context_data(self, **kwargs):
		context = super(StrengtheningView, self).get_context_data(**kwargs)
		context['fortalecimiento'] =  Fortalecimiento.objects.all().last()
		return context

class ModernizationView(TemplateView):
	template_name = 'modernizacion.html'
	def get_context_data(self, **kwargs):
		context = super(ModernizationView, self).get_context_data(**kwargs)
		context['modernizacion'] =   Modernizacion.objects.all().last()
		return context

class ProjectView(TemplateView):
	template_name = 'proyecto.html'
	def get_context_data(self, **kwargs):
		context = super(ProjectView, self).get_context_data(**kwargs)
		context['proyectos'] =  Proyecto.objects.all()
		return context

class GalleryView(TemplateView):
	template_name = 'gallery.html'

class CenterView(TemplateView):
	template_name = 'centroDocumentacion.html'
	def get_context_data(self, **kwargs):
		context = super( CenterView, self).get_context_data(**kwargs)
		context['documentos'] =  Documento.objects.all()
		return context

class ContactView(TemplateView):
	template_name = 'contact.html'

