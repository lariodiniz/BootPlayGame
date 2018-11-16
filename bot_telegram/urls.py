# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.urls import path

from .views import ativaBotView, desativaView

app_name = 'bot_telegram'

urlpatterns = [
    path('ativar/', ativaBotView, name='ativar'),
    path('desativar/', desativaView, name='desativar'),

]
