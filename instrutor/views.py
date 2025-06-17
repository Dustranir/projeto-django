from django.shortcuts import render, redirect, get_object_or_404
from instrutor.models import Instrutor
from instrutor.forms import InstrutorForm, InstrutorAtualizarForm


def listar(request):
    instrutores = Instrutor.objects.all()
    return render(request, 'instrutor/listarInstrutor.html', {'instrutores': instrutores})

# carregar a pagina para cadastrar um titulo na base de dados
def cadastro(request):
    return render(request, 'instrutor/cadastroInstrutor.html')

def cadastrar(request):
    if request.method == 'POST':
        form = InstrutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instrutor:listar')
    else:
        form = InstrutorForm()
    return render(request, 'instrutor/cadastroInstrutor.html', {'form': form})


def carregar_instrutor(request, codigo):
    instrutor = get_object_or_404(Instrutor, pk=codigo)
    form = InstrutorAtualizarForm(instance=instrutor)
    return render(request, 'instrutor/atualizarInstrutor.html', {'form': form, 'instrutor': instrutor})


def atualizar(request, codigo):
    instrutor = get_object_or_404(Instrutor, pk=codigo)

    if request.method == 'POST':
        form = InstrutorAtualizarForm(request.POST, instance=instrutor)
        if form.is_valid():
            form.save()
            return redirect('instrutor:listar')
        else:
            return render(request, 'instrutor/atualizarInstrutor.html', {'form': form, 'instrutor': instrutor})

    return redirect('instrutor:carregar_instrutor', codigo=codigo)
