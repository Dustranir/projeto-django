from django.shortcuts import render
from titulo.models import Titulo
# Create your views here.

def listar(request):
    
    lista_titulos = Titulo.objects.all()
    contexto = {
        'titulos':lista_titulos
    }
    
    return render(request, 'titulo/listarTitulo.html', context= contexto)

def cadastrar(request):
    return render (request, 'titulo/cadastrarTitulo.html')