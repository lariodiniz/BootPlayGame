# coding: utf-8
__author__ = "Lário dos Santos Diniz"


from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings

class AtivaBotViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse('facebook:ativar')
        self.client = Client()

    def test_get_token_is_invalid(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Error, invalid token')

    def test_get_token_is_valid(self):
        response = self.client.get(self.url+"?hub.mode=subscribe&hub.challenge=1360284769&hub.verify_token="+settings.FACEBOOK_BOT_TOKEN)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'1360284769')