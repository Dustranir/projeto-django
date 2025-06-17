# instrutor/urls.py
from django.urls import path
from . import views

app_name = 'instrutor'

urlpatterns = [
    path('', views.listar, name='listar'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('carregar/<int:codigo>/', views.carregar_instrutor, name='carregar_instrutor'),
    path('atualizar/<int:codigo>/', views.atualizar, name='atualizar'),
]
