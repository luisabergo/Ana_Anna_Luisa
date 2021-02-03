"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django_app import views

urlpatterns = [
  url(r'^admin/', include(admin.site.urls)),
  url(r'^django_app/', include('django_app.urls')),
  url(r'^CadastroProfessor/', views.CadastroUsuario, name='CadastroUsuario'),
  url(r'^CadastroDisciplina/', views.CadastroDisciplina, name='CadastroDisciplina'),
  url(r'^CadastroConteudo/', views.CadastroConteudo, name='CadastroConteudo'),
  url(r'^login/', views.login, name='login'),
  url(r'^ajuda/', views.ajuda, name='ajuda'),
  url(r'^CadastroFase/', views.CadastroFase, name='CadastroFase'),
  url(r'^chat/', views.chat, name='chat'),
  url(r'^video/', views.CadastroVideo, name='CadastroVideo'),
  url(r'^texto/', views.CadastroTexto, name='CadastroTexto'),
]
