#coding: utf-8
__author__ = "Lário dos Santos Diniz"


from django.views import View
from django.http import HttpResponse
from django.conf import settings


class AtivaBotView(View):

    def get(self, request, *args, **kwargs):
        if self.request.GET.get(u'hub.verify_token') == settings.FACEBOOK_BOT_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

ativaBotView = AtivaBotView.as_view()
