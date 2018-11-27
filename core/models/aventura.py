# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models


class Aventura(models.Model):

    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descrição', blank=True)

    class Meta:
        verbose_name = 'Aventura'
        verbose_name_plural = 'Aventuras'

    def __str__(self):
        return "{} - {}".format(self.pk, self.nome)