# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models

from core.models import Aventura

class Cena(models.Model):

    aventura = models.ForeignKey(Aventura, verbose_name='Aventura', on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição', blank=True)

    numero = models.PositiveSmallIntegerField("Ordem")

    class Meta:
        verbose_name = 'Cena'
        verbose_name_plural = 'Cenas'

    def __str__(self):
        return "Aventura {} - Cena {} - {}".format(self.aventura, self.numero, self.nome)