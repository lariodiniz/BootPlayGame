#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.contrib import admin

from .models import MensagensPadrao, Aventura, Personagem, Cena, Opcao


class MensagensPadraoAdmin(admin.ModelAdmin):

    list_display = ['mensagem', 'resposta']
    search_fields = ['mensagem', 'resposta']


class AventuraAdmin(admin.ModelAdmin):

    list_display = ['nome', 'descricao']
    search_fields = ['nome', 'descricao']


class PersonagemAdmin(admin.ModelAdmin):

    list_display = ['nome', 'genero', 'genero', 'aventura']
    search_fields = ['nome', 'genero', 'genero', 'aventura']
    list_filter = ['iniciou', 'ultimo_acesso']


class CenaAdmin(admin.ModelAdmin):

    list_display = ['nome', 'aventura', 'numero','descricao']
    search_fields = ['nome', 'aventura','numero', 'descricao']


class OpcaoAdmin(admin.ModelAdmin):

    list_display = ['cena', 'descricao']
    search_fields = ['cena', 'descricao']


admin.site.register(MensagensPadrao, MensagensPadraoAdmin)
admin.site.register(Aventura, AventuraAdmin)
admin.site.register(Personagem, PersonagemAdmin)
admin.site.register(Cena, CenaAdmin)
admin.site.register(Opcao, OpcaoAdmin)