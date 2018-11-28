# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models
from core.models import Aventura

class Jogadores(models.Model):

    STATUS_CHOICES = (
        (0, 'Cadastrando'),
        (1, 'Escolhendo Aventura'),
        (2, 'Criando Personagem'),
        (3, 'Jogando Aventura'),
    )

    id_facebook = models.CharField('Primeiro Nome', max_length=255, blank=True, unique=True)
    primeiro_nome = models.CharField('Primeiro Nome', max_length=50, blank=True)
    ultimo_nome = models.CharField('Ultimo Nome', max_length=50, blank=True)
    iniciou = models.DateTimeField('Iniciou', auto_now_add=True)
    ultimo_acesso = models.DateTimeField('Ultimo Acesso', auto_now=True)
    aventura_atual = models.ForeignKey(Aventura, verbose_name='Aventura Atual', on_delete=models.SET_NULL, null=True)
    status = models.IntegerField('Status',
        choices=STATUS_CHOICES,
        default=0, blank=True)

    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'

    def __str__(self):
        return "{} {}".format(self.primeiro_nome, self.ultimo_nome)