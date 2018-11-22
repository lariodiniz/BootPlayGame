#coding: utf-8
__author__ = "Lário dos Santos Diniz"

import json

from django.views import View
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import generic

from bot_facebook.utils import post_facebook_message


class AtivaBotView(View):

    def get(self, request, *args, **kwargs):

        tokenReqeust = self.request.GET.get(u'hub.verify_token')

        if tokenReqeust:
            tokenReqeust = tokenReqeust.lstrip().rstrip().replace(' ', '')

        if tokenReqeust == settings.FACEBOOK_BOT_TOKEN.lstrip().rstrip().replace(' ', ''):
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    post_facebook_message(message['sender']['id'],
                                          message['message']['text'])
        return HttpResponse()

ativaBotView = AtivaBotView.as_view()
