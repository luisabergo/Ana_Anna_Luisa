from django.shortcuts import render, render_to_response, get_object_or_404
from django_app.models import Blog, Categoria
from django.http import HttpResponse

def index(request):
    return render(request, 'django/index.html')


def CadastroUsuario(request):
    return render(request, 'django/CadastroUsuario.html')

def CadastroDisciplina(request):
    return render(request, 'django/CadastroDisciplina.html')

def CadastroConteudo(request):
    return render(request, 'django/CadastroConteudo.html')

def login(request):
    return render(request, 'django/login.html')

def ajuda(request):
    return render(request, 'django/ajuda.html')

def CadastroFase(request):
    return render(request, 'django/CadastroFase.html')
  
def chat(request):
    return render(request, 'django/chat.html')
def CadastroVideo(request):
    return render(request, 'django/ConteudoVideo.html')

def CadastroTexto(request):
    return render(request, 'django/CadastroTexto.html')
    
def Perfil(request):
    return render(request, 'django/perfil.html')

def InserirComentario(request):
    return render(request, 'django/InserirComentario.html')
