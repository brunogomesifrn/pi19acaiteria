"""pi19acaiteria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import index
from core.views import cardapio, cardapio_listar, cardapio_cadastrar, cardapio_atualizar, cardapio_remover
from core.views import cadastrar_recheio, cadastrar_creme, cadastrar_cobertura, cadastrar_adicional

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    #URLs de Areas
    path('cardapio/', cardapio, name='cardapio'),
    path('cardapio/', cardapio_listar, name='cardapio'),
    path('cardapio_cadastrar/', cardapio_cadastrar, name='cardapio_cadastrar'),
    path('cardapio_atualizar/<int:id>', cardapio_atualizar, name='cardapio_atualizar'),
    path('cardapio_remover/<int:id>', cardapio_remover, name='cardapio_remover'),
    path('cadastrar_recheio/', cadastrar_recheio, name='cadastrar_recheio'),
    path('cadastrar_creme/', cadastrar_creme, name='cadastrar_creme'),
    path('cadastrar_cobertura/', cadastrar_cobertura, name='cadastrar_cobertura'),
    path('cadastrar_adicional/', cadastrar_adicional, name='cadastrar_adicional'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
