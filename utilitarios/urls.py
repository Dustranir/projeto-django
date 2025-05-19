from django.urls import path

from . import views

urlpatterns = [
    path('', views.utilitarios, name = "utilitarios"),  
    path('exibemensagem', views.exibe_mensagem, name="exibir_mensagem")  
]