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

def CadastroConteudo(request):
    return render(request, 'django/CadastroConteudo.html')


