#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from bot_telegram.bot import Bot

telegram = Bot()
class AtivaBotView(LoginRequiredMixin, View):


    def get(self, request):
        telegram.Ativar()
        return HttpResponse('Ativado')

class DesativaView(LoginRequiredMixin, View):


    def get(self, request):
        telegram.Parar()
        return HttpResponse('Desativado')



ativaBotView = AtivaBotView.as_view()
desativaView = DesativaView.as_view()