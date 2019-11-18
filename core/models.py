from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here

class CustomUser(AbstractUser):
	cpf = models.CharField('CPF', max_length=11)

	def __str__(self):
		return self.email

class Cardapio(models.Model):
	nome = models.CharField('Nome', max_length=200)
	preco = models.FloatField('Preco', max_length=5)
	quantidade = models.CharField('Quantidade', max_length=200)
	descrição = models.TextField('Descrição', max_length=3000)
	foto = models.ImageField('Foto', upload_to='media', null=True)

	def __str__(self):
		return self.nome

class Recheios(models.Model):
	nome = models.CharField('Nome', max_length=200)
	foto = models.ImageField('Foto', upload_to='recheio', null=True)

	def __str__(self):
		return self.nome

class Coberturas(models.Model):
	nome = models.CharField('Nome', max_length=200)
	foto = models.ImageField('Foto', upload_to='cobertura', null=True)

	def __str__(self):
		return self.nome

class Cremes(models.Model):
	nome = models.CharField('Nome', max_length=200)
	foto = models.ImageField('Foto', upload_to='creme', null=True)

	def __str__(self):
		return self.nome

class Adicionais(models.Model):
	nome = models.CharField('Nome', max_length=200)
	preco = models.FloatField('Preco', max_length=5)
	foto = models.ImageField('Foto', upload_to='adicional', null=True)

	def __str__(self):
		return self.nome
