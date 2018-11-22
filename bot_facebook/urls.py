# coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.urls import path

from .views import ativaBotView

app_name = 'bot_facebook'

urlpatterns = [
    path('ativar/', ativaBotView, name='ativar'),
    path('ativar', ativaBotView, name='app'),
]


