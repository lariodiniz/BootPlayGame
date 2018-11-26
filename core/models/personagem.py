# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.db import models

from bot_facebook.models import Jogadores as Jogadores_F
from bot_telegram.models import Jogadores as Jogadores_T
from core.models import Aventura


class Personagem(models.Model):

    GENERO_CHOICES = (
        (0, 'Homem'),
        (1, 'Mulher'),
        (2, 'Outro'),
    )

    jogadorF = models.ForeignKey(Jogadores_F, verbose_name='Jogador Facebook', on_delete=models.CASCADE)
    jogadorT = models.ForeignKey(Jogadores_T, verbose_name='Jogador Telegram', on_delete=models.CASCADE)
    aventura = models.ForeignKey(Aventura, verbose_name='Aventura', on_delete=models.CASCADE)
    cena = models.PositiveSmallIntegerField("Cena", blank=True, null=True)
    nome = models.CharField('Nome', max_length=50)
    iniciou = models.DateTimeField('Iniciou', auto_now_add=True)
    ultimo_acesso = models.DateTimeField('Ultimo Acesso', auto_now=True)
    genero = models.IntegerField('Genero',
        choices=GENERO_CHOICES,
        default=0, blank=True)

    class Meta:
        verbose_name = 'Personagem'
        verbose_name_plural = 'Personagens'

    def __str__(self):
        return self.nome
