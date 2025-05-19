from django.urls import path

from . import views

urlpatterns = [
    path('', views.instrutor, name = "instrutor"),  
    path('exibemensagem', views.exibe_mensagem, name="exibir_mensagem")  
]