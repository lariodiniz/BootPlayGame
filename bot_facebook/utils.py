#coding: utf-8
__author__ = "Lário dos Santos Diniz"


import json
import requests
from django.conf import settings
from bot_facebook.models import Jogadores

class BotFacebook:

    def __init__(self, id_usuario, mensagem_usuario):

        if mensagem_usuario == "/start":
            self._verificaJogador(id_usuario)


    def _verificaJogador(self, id_usuario):

        if Jogadores.objects.filter(id=id_usuario).exists():
            mensagem = "Você já é um jogador cadastrado."
            self._send_message(id_usuario, mensagem)
        else:
            mensagem = "Você não é um jogador cadastrado. Estamos te cadastrando..."
            contador = 0

            while contador < 3:
                self._send_message(id_usuario, mensagem)
                self.__CadastraJogador()
                if Jogadores.objects.filter(id=self.__telegram_id).exists():
                    mensagem = "Você foi cadastrado com sucesso."
                    self._send_message(id_usuario, mensagem)
                    contador = 4
                elif contador < 2:
                    mensagem = "Aconteceu um problema no cadastro, vamos tentar mais uma vez."
                    self._send_message(id_usuario, mensagem)
                elif contador == 2:
                    mensagem = "Aconteceu um problema no cadastro, vamos tentar uma ultima vez."
                    self._send_message(id_usuario, mensagem)
                contador += 1
            if contador == 3:
                mensagem = "Não conseguimos te cadastrar, por favor, tente de novo mais tarde."
                self._send_message(id_usuario, mensagem)


    def _send_message(fbid, recevied_message):
        post_message_url = 'https://graph.facebook.com/v2.6/me/messages?' \
                       'access_token={}'.format(settings.FACEBOOK_BOT_TOKEN.lstrip().rstrip().replace(' ', ''))
        response_msg = json.dumps({"recipient": {"id": fbid},
                               "message": {"text": recevied_message}})
        requests.post(post_message_url,
                           headers={"Content-Type": "application/json"},
                           data=response_msg)