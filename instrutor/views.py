from django.shortcuts import render
from instrutor.models import Instrutor

# Create your views here.

def listar(request):
    return render(request, 'instrutor/listarInstrutor.html')

def cadastrar(request):
    return render (request, 'instrutor/cadastrarInstrutor.html')

