from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View
from .models import Inicio, QuienesSomo, Contacto, Proyecto, Documento, Paz, Comunidade, Fortalecimiento, Modernizacion,Imagene
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.contrib import messages
from django.conf import settings


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


def DetailProject(request, id):
	detalleProject = Proyecto.objects.filter(pk=id)
	return render(request, "detailProject.html", {'detalleProject': detalleProject})


class GalleryView(TemplateView):
	template_name = 'gallery.html'

	def get_context_data(self, **kwargs):
		context = super(GalleryView, self).get_context_data(**kwargs)
		context['imagenes'] =  Imagene.objects.all()
		return context

class CenterView(TemplateView):
	template_name = 'centroDocumentacion.html'
	def get_context_data(self, **kwargs):
		context = super( CenterView, self).get_context_data(**kwargs)
		context['documentos'] =  Documento.objects.all()
		return context


def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            print subject
            from_email = form.cleaned_data['from_email']
            print from_email
            message = form.cleaned_data['message']
            print message
            try:
            	print "entro"
                send_mail(subject, message, from_email,[settings.EMAIL_HOST_USER])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            
    return render(request, "contact.html", {'form': form})

