# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.test import TestCase
from model_mommy import mommy

from core.models import MensagensPadrao

class JMensagensPadraoTestCase(TestCase):
    """Classe que testa o modelo Jogadores"""

    def setUp(self):
        """Método Inicial"""

        self.mensagem = mommy.make(MensagensPadrao, mensagem="teste", resposta="respondendo a teste")

    def tearDown(self):
        """Método Finaliza"""
        self.mensagem.delete()

    def test_existe_campos(self):
        """testa se existe no modelo o campo Nome"""
        self.assertTrue('mensagem' in dir(MensagensPadrao), 'Classe MensagensPadrao não tem o campo mensagem')
        self.assertTrue('resposta' in dir(MensagensPadrao), 'Classe MensagensPadrao não tem o campo resposta')


    def test_existe_mensagem_madrao(self):
        """testa se esta criando jogador corretamente"""

        self.assertEquals(MensagensPadrao.objects.count(), 1)
        self.assertEquals(MensagensPadrao.objects.all()[0].mensagem, self.mensagem.mensagem)
        self.assertEquals(MensagensPadrao.objects.all()[0].resposta, self.mensagem.resposta)