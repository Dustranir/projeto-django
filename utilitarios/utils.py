from tiposdeatividade.models import TiposDeAtividade
from titulo.models import Titulo
from aluno.models import Aluno
from instrutor.models import Instrutor
from turma.models import Turma
from django.db import connection

# Função de truncar tabelas para zerar o contador de auto incremento:

def truncate_table(nome_tabela):
    with connection.cursor() as cursor:
        cursor.execute (f'DELETE FROM {nome_tabela}')
        cursor.execute (f'DELETE FROM sqlite_sequence EHERE name = "{nome_tabela}"')

def truncar_tabelas():
    truncate_table('turma_turma')
    truncate_table('instrutor_instrutor')
    truncate_table('aluno_aluno')
    truncate_table('titulo_titulo')
    truncate_table('tiposdeatividade_tiposdeatividade')


def popular_tiposdeatividade():
    lista_tiposdeatividade = []
    
    for i in range(0,10):
        lista_tiposdeatividade.append(TiposDeAtividade(descricao='Atividade ' + f'{i:02}'))
        
    TiposDeAtividade.objects.bulk_create(lista_tiposdeatividade)

def popular_titulo():
    lista_titulo = []

    for i in range(0,10):
        lista_titulo.append(Titulo(descricao='Titulo ' + f'{i:02}'))
        
    Titulo.objects.bulk_create(lista_titulo)

def popular_aluno():
    lista_aluno = []

    for i in range(0,10):
        lista_aluno.append(Titulo(descricao='Aluno ' + f'{i:02}'))
        
    Aluno.objects.bulk_create(lista_aluno)

def popular_instrutor():
    lista_instrutor = []

    for i in range(0,10):
        lista_instrutor.append(Titulo(descricao='Instrutor ' + f'{i:02}'))
        
    Titulo.objects.bulk_create(lista_instrutor)

def popular_turma():
    lista_turma = []

    for i in range(0,10):
        lista_turma.append(Titulo(descricao='Turma ' + f'{i:02}'))
        
    Titulo.objects.bulk_create(lista_turma)
