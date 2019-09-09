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
	
	return render(request, 'cardapio_lista.html', contexto)

def recheio_listar(request):
	recheio = Recheios.objects.all()
	contexto = {
	'recheio_listar': recheio
	}
	
	return render(request, 'cardapio_lista.html', contexto) 

def creme_listar(request):
	creme = Cremes.objects.all()
	contexto = {
	'creme_listar': recheio
	}
	
	return render(request, 'cardapio_lista.html', contexto) 		 

#cruds de açaís

def cardapio_cadastrar(request):
	form = CardapioForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('cardapio_listar')
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
		return redirect('cardapio_listar')
	contexto = {
	    'form': form
	}
	return render(request, 'cadastro_cardapio.html', contexto)	

def cardapio_remover(request, id):
	cardapio = Cardapio.objects.get(pk=id)
	cardapio.delete()
	return redirect('cardapio_listar')

#cruds de recheio	

def cadastrar_recheio(request):
	form = RecheiosForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('cardapio_listar')
	form = RecheiosForm()
	contexto = {
		'form' : form
	}
	return render(request, 'cadastro_recheio.html', contexto)

def recheio_atualizar(request, id):
	form = Recheios.objects.get(pk=id)
	form = RecheiosForm(request.POST or None, instance=form)
	if form.is_valid():
		form.save()
		return redirect('cardapio_listar')
	contexto = {
	    'form': form
	}
	return render(request, 'cadastro_recheio.html', contexto)

def recheio_remover(request, id):
	recheio = Recheios.objects.get(pk=id)
	recheio.delete()
	return redirect('cardapio_listar')	

#cruds de creme

def cadastrar_creme(request):
	form = CremesForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('cardapio_listar')
	form = CremesForm()
	contexto = {
		'form' : form
	}
	return render(request, 'cadastro_creme.html', contexto)

def creme_atualizar(request, id):
	form = Cremes.objects.get(pk=id)
	form = CremesForm(request.POST or None, instance=form)
	if form.is_valid():
		form.save()
		return redirect('cardapio_listar')
	contexto = {
	    'form': form
	}
	return render(request, 'cadastro_recheio.html', contexto)	

def creme_remover(request, id):
	creme = Cremes.objects.get(pk=id)
	creme.delete()
	return redirect('cardapio_listar')	


#crud de cobertura

def cadastrar_cobertura(request):
	form = CoberturasForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('cardapio')
	form = CoberturasForm()
	contexto = {
		'form' : form
	}
	return render(request, 'cadastro_cobertura.html', contexto)	

#crud de adicional

def cadastrar_adicional(request):
	form = AdicionaisForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('cardapio')
	form = AdicionaisForm()
	contexto = {
		'form' : form
	}
	return render(request, 'cadastro_adicional.html', contexto)