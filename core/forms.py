from django import forms
from django.forms import ModelForm
from .models import Cardapio, Recheios, Coberturas, Cremes, Adicionais


class CardapioForm(ModelForm):
    class Meta():
        model = Cardapio
        fields = ['nome', 'preco', 'quantidade', 'descrição', 'foto']

class RecheiosForm(ModelForm):
    class Meta():
        model = Recheios
        fields = ['nome', 'foto']

class CoberturasForm(ModelForm):
    class Meta():
        model = Coberturas
        fields = ['nome', 'foto']

class CremesForm(ModelForm):
    class Meta():
        model = Cremes
        fields = ['nome', 'foto']

class AdicionaisForm(ModelForm):
    class Meta():
        model = Adicionais
        fields = ['nome', 'preco', 'foto']                