from django.db import models

# Create your models here

class Cardapio(models.Model):
	nome = models.CharField('Nome', max_length=200)
	preco = models.FloatField('Preco', max_length=5)
	quantidade = models.CharField('Quantidade', max_length=200)
	descrição = models.TextField('Descrição', max_length=3000)
	foto = models.ImageField('Foto', upload_to='cursos', null=True)

	def __str__(self):
		return self.nome