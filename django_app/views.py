from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    dicionario_contexto = {'msgnegrito': "Testando fonte em negrito..."}
    return render(request, 'django/index.html', dicionario_contexto)


def CadastroProfessor(request):
    dicionario_contexto1 = {'msgnegrito': "Testando fonte em negrito..."}
    return render(request, 'django/CadastroProfessor.html', dicionario_contexto1)


def CadastroAluno(request):
    dicionario_contexto1 = {'msgnegrito': "Testando fonte em negrito..."}
    return render(request, 'django/CadastroAluno.html', dicionario_contexto1)

def CadastroDisciplina(request):
    dicionario_contexto1 = {'msgnegrito': "Testando fonte em negrito..."}
    return render(request, 'django/CadastroDisciplina.html', dicionario_contexto1)