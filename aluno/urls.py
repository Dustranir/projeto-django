from django.urls import path

from . import views

urlpatterns = [
    path('', views.aluno, name = "aluno"),  
    path('exibemensagem', views.exibe_mensagem, name="exibir_mensagem")  
]