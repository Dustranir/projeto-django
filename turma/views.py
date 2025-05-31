from django.shortcuts import render

# Create your views here.

def listar(request):
    return render(request, 'turma/listarTurma.html')

def cadastrar(request):
    return render (request, 'turma/cadastrarTurma.html')