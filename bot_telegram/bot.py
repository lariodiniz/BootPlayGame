#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from bootplaygame import settings
import requests
import datetime
from bot_telegram.models import Jogadores

class BotTelegram():

    def __init__(self):
        self.api_url = "https://api.telegram.org/bot{}/".format(settings.TELEGRAM_BOT_TOKEN)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update


class Bot():

    def __Agora(self):
        self.__now = datetime.datetime.now()

    def __init__(self):
        self.__bot = BotTelegram()
        self.__Agora()


    def __CadastraJogador(self):
        jogador = Jogadores()
        jogador.nome = self.__telegram_nome
        jogador.id = int(self.__telegram_id)
        jogador.save()

    def __Start(self):
        mensagem = 'Seja bem vindo ao PlayGame RPG, estamos preparando a sua aventura {}\n'.format(self.__telegram_nome)
        mensagem += 'Por favor, espere um minuto.'
        self.__bot.send_message(self.__telegram_id, mensagem)

        if Jogadores.objects.filter(id=self.__telegram_id).exists():
            mensagem = "Você já é um jogador cadastrado."
            self.__bot.send_message(self.__telegram_id, mensagem)
        else:
            mensagem = "Você não é um jogador cadastrado. Estamos te cadastrando..."
            contador = 0

            while contador < 3:
                self.__bot.send_message(self.__telegram_id, mensagem)
                self.__CadastraJogador()
                if Jogadores.objects.filter(id=self.__telegram_id).exists():
                    mensagem = "Você foi cadastrado com sucesso."
                    self.__bot.send_message(self.__telegram_id, mensagem)
                    contador = 4
                elif contador < 2:
                    mensagem = "Aconteceu um problema no cadastro, vamos tentar mais uma vez."
                    self.__bot.send_message(self.__telegram_id, mensagem)
                elif contador == 2:
                    mensagem = "Aconteceu um problema no cadastro, vamos tentar uma ultima vez."
                    self.__bot.send_message(self.__telegram_id, mensagem)
                contador += 1
            if contador == 3:
                mensagem = "Não conseguimos te cadastrar, por favor, tente de novo mais tarde."
                self.__bot.send_message(self.__telegram_id, mensagem)

    def Ativar(self):
        novas_mensagens = None
        today = self.__now.day
        hour = self.__now.hour

        while True:
            self.__bot.get_updates(novas_mensagens)

            ultimas_mensagens = self.__bot.get_last_update()

            self.__ultimas_mensagens_id = ultimas_mensagens['update_id']
            self.__mensagem = ultimas_mensagens['message']['text']
            self.__telegram_id = ultimas_mensagens['message']['chat']['id']
            self.__telegram_nome = ultimas_mensagens['message']['chat']['first_name']

            if self.__mensagem.lower() == '/start':
                self.__Start()

            novas_mensagens = self.__ultimas_mensagens_id + 1

