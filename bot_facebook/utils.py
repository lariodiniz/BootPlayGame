#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from pprint import pprint
import json
import requests
from django.conf import settings
from bot_facebook.models import Jogadores
from core.models import MensagensPadrao

class BotFacebook:

    def __init__(self, id_usuario, mensagem_usuario):

        self.id_usuario = id_usuario
        self.mensagem_usuario = mensagem_usuario

        if not self._MensagensPadrao():
            if mensagem_usuario.lower() in ['oi', 'ola', 'hello']:
                mensagem = "Olá, seja bem vindo a pagina Dados & Desventuras.\nGostaria de jogar uma Aventura de RPG pelo messenger?"
                mensagem += "\n\n"
                mensagem += 'Responda "Sim" para jogar.'
                self._send_message(mensagem)


    def _MensagensPadrao(self):
        mensagensPadrao = MensagensPadrao.objects.all()
        for mensagempadrao in mensagensPadrao:
            if mensagempadrao.mensagem.lower() in self.mensagem_usuario.lower():
                self._send_message(mensagempadrao.resposta)


    def _CadastraJogador(self):
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

            self._send_message(mensagem)
            self.__CadastraJogador()
            if Jogadores.objects.filter(id=self.id_usuario).exists():
                mensagem = "Você foi cadastrado com sucesso."
                self._send_message(mensagem)

            else:
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