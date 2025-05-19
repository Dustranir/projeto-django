from django.urls import path

from . import views

urlpatterns = [
    path('', views.titulo, name = "titulo"),  
    path('exibemensagem', views.exibe_mensagem, name="exibir_mensagem")  
]