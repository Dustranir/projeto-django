from django import forms

# classe formulario inclusao
class TituloForm(forms.Form):
    descricao = forms.CharField(max_length=100,
                                required=True,
                                help_text='Informe a descrição do Título')
    
class TituloAtualizarForm(forms.Form):
    descricao = forms.CharField(max_length=100,
                                required=True,
                                help_text='Informe a descrição do Título')
    codigo = forms.IntegerField(required=True,
                                help_text='Informe o código do Título')
    