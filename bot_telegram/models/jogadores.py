# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models

class Jogadores(models.Model):

    nome = models.CharField('nome', max_length=50)
    iniciou = models.DateTimeField('Iniciou', auto_now_add=True)
    ultimo_acesso = models.DateTimeField('Ultimo Acesso', auto_now=True)