# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models

from core.models import Cena

class Opcao(models.Model):

    cena = models.ForeignKey(Cena, verbose_name='Cena', on_delete=models.CASCADE)
    descricao = models.TextField('Descrição', blank=True)

    proxima_cena = models.ForeignKey(Cena, verbose_name='Cena', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Opção'
        verbose_name_plural = 'Opções'

    def __str__(self):
        return self.descricao