# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.test import TestCase
from model_mommy import mommy

from bot_telegram.models import Jogadores

class JogadoresTestCase(TestCase):
    """Classe que testa o modelo Jogadores"""

    def setUp(self):
        """Método Inicial"""

        self.jogador = mommy.make(Jogadores, nome="Zézinho")

    def tearDown(self):
        """Método Finaliza"""
        self.jogador.delete()

    def test_existe_campos(self):
        """testa se existe no modelo o campo Nome"""
        self.assertTrue('nome' in dir(Jogadores), 'Classe Jogadores não tem o campo nome')
        self.assertTrue('iniciou' in dir(Jogadores), 'Classe Jogadores não tem o campo iniciou')
        self.assertTrue('ultimo_acesso' in dir(Jogadores), 'Classe Jogadores não tem o campo ultimo_acesso')

    def test_existe_jogador(self):
        """testa se esta criando jogador corretamente"""

        self.assertEquals(Jogadores.objects.count(), 1)
        self.assertEquals(Jogadores.objects.all()[0].nome, self.jogador.nome)