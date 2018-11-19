#coding: utf-8
__author__ = "Lário dos Santos Diniz"


from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin



class AtivaBotView(LoginRequiredMixin, View):

    def get(self, request):

        return HttpResponse('Ativado')

ativaBotView = AtivaBotView.as_view()
