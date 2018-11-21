#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.contrib import admin
from django.urls import path, include

from core.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('telegram/', include('bot_telegram.urls', namespace='telegram')),
    path('facebook/', include('bot_facebook.urls', namespace='facebook')),
]
