from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Cardapio, Recheios, Coberturas, Cremes, Adicionais, CustomUser

class customUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'cpf')
        widgets = {
            'cpf': forms.TextInput(attrs={'placeholder': 'Somente números'})
        }

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
