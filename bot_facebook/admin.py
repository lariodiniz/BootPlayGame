#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.contrib import admin

from .models import Jogadores

class JogadoresAdmin(admin.ModelAdmin):

    list_display = ['primeiro_nome', 'ultimo_nome', 'iniciou', 'ultimo_acesso', 'status']
    search_fields = ['primeiro_nome', 'ultimo_nome', 'slug']
    list_filter = ['iniciou', 'ultimo_acesso']

admin.site.register(Jogadores, JogadoresAdmin)