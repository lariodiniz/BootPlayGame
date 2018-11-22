#coding: utf-8
__author__ = "Lário dos Santos Diniz"


import json
import requests
from django.conf import settings
from bot_facebook.models import Jogadores

class BotFacebook:

    def __init__(self, id_usuario, mensagem_usuario):

        self.id_usuario = id_usuario
        self.mensagem_usuario = mensagem_usuario

        if mensagem_usuario.lower in ['oi', 'ola', 'hello']:
            mensagem = "Olá, seja bem vindo a pagina Dados & Desventuras.\n Gostaria de jogar uma Aventura de RPG?"
            self._send_message(mensagem)

        elif mensagem_usuario == "/start":
            self._verificaJogador()


    def __CadastraJogador(self):
        jogador = Jogadores()
        jogador.nome = "Facebook"
        jogador.id = int(self.id_usuario)
        jogador.save()

    def _verificaJogador(self):

        if Jogadores.objects.filter(id=self.id_usuario).exists():
            mensagem = "Você já é um jogador cadastrado."
            self._send_message(mensagem)
        else:
            mensagem = "Você não é um jogador cadastrado. Estamos te cadastrando..."
            contador = 0

            while contador < 3:
                self._send_message(mensagem)
                self.__CadastraJogador()
                if Jogadores.objects.filter(id=self.id_usuario).exists():
                    mensagem = "Você foi cadastrado com sucesso."
                    self._send_message(mensagem)
                    contador = 4
                elif contador < 2:
                    mensagem = "Aconteceu um problema no cadastro, vamos tentar mais uma vez."
                    self._send_message(mensagem)
                elif contador == 2:
                    mensagem = "Aconteceu um problema no cadastro, vamos tentar uma ultima vez."
                    self._send_message(mensagem)
                contador += 1
            if contador == 3:
                mensagem = "Não conseguimos te cadastrar, por favor, tente de novo mais tarde."
                self._send_message(mensagem)


    def _send_message(self, mensagem):
        post_message_url = 'https://graph.facebook.com/v2.6/me/messages?' \
                       'access_token={}'.format(settings.FACEBOOK_BOT_TOKEN.lstrip().rstrip().replace(' ', ''))
        response_msg = json.dumps({"recipient": {"id": self.id_usuario},
                               "message": {"text": mensagem}})
        requests.post(post_message_url,
                           headers={"Content-Type": "application/json"},
                           data=response_msg)