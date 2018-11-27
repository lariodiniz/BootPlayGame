#coding: utf-8
__author__ = "Lário dos Santos Diniz"

import json
import requests
from django.conf import settings


class Service:

    def __init__(self, id_usuario):
        self.id_usuario = id_usuario
        self.url = 'https://graph.facebook.com/v2.6/'

    def BuscaDadosUsuario(self):
        get_message_url = self.url+str(self.id_usuario)+'?access_token={}'.format(settings.FACEBOOK_BOT_TOKEN.lstrip().rstrip().replace(' ', ''))
        retorno = requests.get(get_message_url)

        return retorno.json()

    def EnviaMensagem(self, mensagem):
        post_message_url = self.url+'me/messages?' \
                       'access_token={}'.format(settings.FACEBOOK_BOT_TOKEN.lstrip().rstrip().replace(' ', ''))
        response_msg = json.dumps({"recipient": {"id": self.id_usuario},
                               "message": {"text": mensagem}})
        requests.post(post_message_url,
                           headers={"Content-Type": "application/json"},
                           data=response_msg)