from django.shortcuts import render

# Create your views here.

def listar(request):
    return render(request, 'titulo/listarTitulo.html')

def cadastrar(request):
    return render (request, 'titulo/cadastrarTitulo.html')