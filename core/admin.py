#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.contrib import admin

from .models import MensagensPadrao

class MensagensPadraoAdmin(admin.ModelAdmin):

    list_display = ['mensagem', 'resposta']
    search_fields = ['mensagem', 'resposta']


admin.site.register(MensagensPadrao, MensagensPadraoAdmin)