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
	recheio = Recheios.objects.all()
	cobertura = Coberturas.objects.all()
	creme = Cremes.objects.all()

	contexto = {
	#'cardapio_listar': cardapio,
	'recheio': recheio,
	'cobertura':cobertura,
	'creme':creme
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
		return redirect('cardapio_listar')
	form = CoberturasForm ()
	contexto = {
		'form' : form
	}
	return render(request, 'cadastro_cobertura.html', contexto)

def cobertura_atualizar(request, id):
	form = Coberturas.objects.get(pk=id)
	form = CoberturasForm(request.POST or None, instance=form)
	if form.is_valid():
		form.save()
		return redirect('cardapio_listar')
	contexto = {
	    'form': form
	}
	return render(request, 'cadastro_cobertura.html', contexto)

def cobertura_remover(request, id):
	cobertura = Coberturas.objects.get(pk=id)
	cobertura.delete()
	return redirect('cardapio_listar')

#crud de adicional

def cadastrar_adicional(request):
	form = AdicionaisForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('cardapio_listar')
	form = AdicionaisForm()
	contexto = {
		'form' : form
	}
	return render(request, 'cadastro_adicional.html', contexto)

def adicional_atualizar(request, id):
	form = Adicionais.objects.get(pk=id)
	form = AdicionaisForm(request.POST or None, instance=form)
	if form.is_valid():
		form.save()
		return redirect('cardapio_listar')
	contexto = {
	    'form': form
	}
	return render(request, 'cadastro_cobertura.html', contexto)

def adicional_remover(request, id):
	adicional = Adicionais.objects.get(pk=id)
	adicional.delete()
	return redirect('cardapio_listar')
