from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name="index"), #search
    url(r'^quienes-somos/$', views.AboutView.as_view(), name="about"),
    url(r'^paz-seguridad/$', views.PeaceView.as_view(), name="peace"),
    url(r'^comunidades-y-medio-ambiente/$', views.CommunityView.as_view(), name="community"),
    url(r'^fortalecimiento-institucional/$', views.StrengtheningView.as_view(), name="strengthening"),
  	url(r'^modernizacion-de-gobiernos/$', views.ModernizationView.as_view(), name="modernization"),
    url(r'^proyectos/$', views.ProjectView.as_view(), name="project"),
    url(r'^galerias/$', views.GalleryView.as_view(), name="gallery"),
    url(r'^centro-documentacion/$', views.CenterView.as_view(), name="center"),
    url(r'^contactos/$', views.ContactView.as_view(), name="contact"),    
)