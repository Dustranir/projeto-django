from django.shortcuts import render

# Create your views here.

def instrutor(request):
    return render(request, 'instrutor/listarInstrutor.html')