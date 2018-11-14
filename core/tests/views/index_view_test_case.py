# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.test import TestCase, Client
from django.urls import reverse

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def tearDown(self):
        pass

    def test_status_code(self):
        """
        Testa se retorna um status code 200
        """
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_used(self):
        """
        Testa se o template utilizado é o core/index.html
        """
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'core/index.html')

    def test_info_template(self):
        """
        testa se o botão do telegram esta na tela.
        """
        response = self.client.get(self.url)
        self.assertContains(response, 'O <strong>BotPlayGame</strong> é um bot desenvolvido para você jogar')
        self.assertContains(response, 'https://t.me/EscolhasBot')
