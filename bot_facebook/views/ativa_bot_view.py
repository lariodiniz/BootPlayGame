#coding: utf-8
__author__ = "Lário dos Santos Diniz"


from django.views import View
from django.http import HttpResponse
from django.conf import settings


class AtivaBotView(View):

    def get(self, request, *args, **kwargs):

        tokenReqeust = self.request.GET.get(u'hub.verify_token')

        if tokenReqeust:
            tokenReqeust = tokenReqeust.lstrip().rstrip().replace(' ', '')

        if tokenReqeust == settings.FACEBOOK_BOT_TOKEN.lstrip().rstrip().replace(' ', ''):
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('{}<br>{}'.format(tokenReqeust, settings.FACEBOOK_BOT_TOKEN.lstrip().rstrip().replace(' ', '')))

ativaBotView = AtivaBotView.as_view()
