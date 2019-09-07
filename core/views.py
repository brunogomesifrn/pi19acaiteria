from django.shortcuts import render, redirect
from .models import Cardapio, Recheios, Coberturas, Cremes, Adicionais
from .forms import CardapioForm, RecheiosForm, CoberturasForm, CremesForm, AdicionaisForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings



def index(request):
	return render (request, 'index.html')


def cardapio(request):
	return render(request, 'cardapio.html')

def cardapio_listar(request):
	cardapio = Cardapio.objects.all()
	contexto = {
	    'cardapio_listar': cardapio

	}
	return render(request, 'cardapio.html', contexto)

def cardapio_cadastrar(request):
	form = CardapioForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('cardapio')
	form = CardapioForm()
	contexto = {
		'form' : form
	}
	return render(request, 'cadastro_cardapio.html', contexto)

def cardapio_atualizar(request, id):
	cardapio = Cardapio.objects.get(pk=id)
	form = CardapioForm(request.POST or None, instance=cardapio)
	if form.is_valid():
		form.save()
		return redirect('cardapio')
	contexto = {
	    'form': form
	}
	return render(request, 'cadastro_cardapio.html', contexto)	

def cardapio_remover(request, id):
	cardapio = Cardapio.objects.get(pk=id)
	cardapio.delete()
	return redirect('cardapio')

def cadastrar_recheio(request):
	form = CardapioForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('cardapio')
	form = CardapioForm()
	contexto = {
		'form' : form
	}
	return render(request, 'cadastro_recheio.html', contexto)

