#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from bootplaygame import settings
import requests
import datetime

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


greetings = ('hello', 'hi', 'greetings', 'sup')

class Bot():

    def __agora(self):
        self.__now = datetime.datetime.now()

    def __init__(self):
        self.__bot = BotTelegram()
        self.__agora()

    def Ativar(self):
        novas_mensagens = None
        today = self.__now.day
        hour = self.__now.hour

        while True:
            self.__bot.get_updates(novas_mensagens)

            ultimas_mensagens = self.__bot.get_last_update()

            ultimas_mensagens_id = ultimas_mensagens['update_id']
            mensagem = ultimas_mensagens['message']['text']
            telegram_id = ultimas_mensagens['message']['chat']['id']
            telegram_nome = ultimas_mensagens['message']['chat']['first_name']

            print(mensagem.lower())
            if mensagem.lower() in greetings and today == self.__now.day and 6 <= hour < 12:
                self.__bot.send_message(telegram_id, 'Good Morning  {}'.format(telegram_nome))
                today += 1

            elif mensagem.lower() in greetings and today == self.__now.day and 12 <= hour < 17:
                self.__bot.send_message(telegram_id, 'Good Afternoon {}'.format(telegram_nome))
                today += 1

            elif mensagem.lower() in greetings and today == self.__now.day and 17 <= hour < 23:
                self.__bot.send_message(telegram_id, 'Good Evening  {}'.format(telegram_nome))
                today += 1

            novas_mensagens = ultimas_mensagens_id + 1