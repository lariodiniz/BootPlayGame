#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'core/index.html'


index = IndexView.as_view()