# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models


class MensagensPadrao(models.Model):

    mensagem = models.CharField('mensagem', max_length=255)
    resposta = models.CharField('resposta', max_length=255)
