from django.shortcuts import HttpResponse

# Create your views here.

def utilitarios(request):
    return HttpResponse("Olá! Eu sou a página Utilitarios")

def exibe_mensagem(request):
    t_html = '<!DOCTYPE html> <html lang="pt-BR"> <head>     <meta charset="UTF-8">     <meta name="viewport" content="width=device-width, initial-scale=1.0">     <title>Escola</title> </head> <body>     <p>Esta é minha página de índice</p> </body> </html>'
    return HttpResponse(t_html)

#'<html><body>Ola</body></html>'