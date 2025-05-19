from django.urls import path

from . import views

urlpatterns = [
    path('', views.turma, name = "turma"),  
    path('exibemensagem', views.exibe_mensagem, name="exibir_mensagem")  
]