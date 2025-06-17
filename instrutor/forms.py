from django import forms
from .models import Instrutor

class InstrutorForm(forms.ModelForm):
    class Meta:
        model = Instrutor
        fields = ['nome', 'descricao']  # Ajuste conforme os campos do modelo


class InstrutorAtualizarForm(forms.ModelForm):
    class Meta:
        model = Instrutor
        fields = ['nome', 'descricao']  # Mesmo campos ou apenas os editáveis