from django.shortcuts import render
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

def chat(request):
    return render(request, 'django/chat.html')

def CadastroFase(request):
    return render(request, 'django/CadastroFase.html')
