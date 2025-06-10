from tiposdeatividade.models import TiposDeAtividade
from titulo.models import Titulo
from aluno.models import Aluno
from instrutor.models import Instrutor
from turma.models import Turma
from django.db import connection
from datetime import date
import random

#Gerar valor aleatório
def gerar_numero_aleatorio_faixa(inicio, fim):
    return random.randint(inicio, fim)

def gerar_numero_aleatorio_sequencia(lista_valores):
    return random.choice(lista_valores)

#Gerar data aleatória:

def gerar_data_aleatoria(tipo_data):
    dia= gerar_numero_aleatorio_faixa(1,28)
    mes = gerar_numero_aleatorio_faixa(1,12)
    ano = 0
    
    if tipo_data=='inicial':
        ano = gerar_numero_aleatorio_faixa(1970,2007)
    elif tipo_data =='final':
        ano = gerar_numero_aleatorio_faixa(2021,2024)
    elif tipo_data =='nascimento':
        ano = gerar_numero_aleatorio_faixa(1970,2000)
    else:
        ano= gerar_numero_aleatorio_faixa(1970, 2025)
        
    return date(ano, mes, dia)

#Gerar RG aleatório:

def gerar_rg_aleatorio():
    random.randint(100000000, 999999999)
    
#Gerar Tel aleatório:

def gerar_tel_aleatorio():
    random.randint(100000000, 999999999)
    
def gerar_ddd_aleatorio():
    random.randint(11,71)
    

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
        lista_aluno.append(Aluno(descricao='Aluno ' + f'{i:02}', 
                                 data_inicial = gerar_data_aleatoria('inicial')))
        
    Aluno.objects.bulk_create(lista_aluno)

def popular_instrutor():
    lista_instrutor = []
    
    lista_codigos_titulo = Titulo.objects.values_list('codigo', flat = True)
    codigo_selecionado = gerar_numero_aleatorio_sequencia(lista_codigos_titulo)
    titulo = Titulo.objects.get(pk=codigo_selecionado)

    for i in range(0,10):
        lista_instrutor.append(Instrutor(nome='Instrutor ' + f'{i:02}',
                                        data_nascimento = gerar_data_aleatoria('nascimento'),
                                        rg='RG ' + gerar_rg_aleatorio(),
                                        telefone = 'Tel ' + gerar_tel_aleatorio(),
                                        DDD = 'DDD ' + gerar_ddd_aleatorio(),
                                        codigo_titulo = titulo
                                        )
                               )
        
    Instrutor.objects.bulk_create(lista_instrutor)

def popular_turma():
    lista_turma = []

    for i in range(0,10):
        lista_turma.append(Turma(descricao='Turma ' + f'{i:02}'))
        
    Turma.objects.bulk_create(lista_turma)
