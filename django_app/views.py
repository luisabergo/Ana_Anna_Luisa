from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'django/index.html')


def CadastroProfessor(request):
    return render(request, 'django/CadastroProfessor.html')


def CadastroAluno(request):
    return render(request, 'django/CadastroAluno.html')

def CadastroDisciplina(request):
    return render(request, 'django/CadastroDisciplina.html')
    
def login(request):
    return render(request, 'django/login.html')

def ajuda(request):
    return render(request, 'django/ajuda.html')

def chat(request):
    return render(request, 'django/chat.html')
