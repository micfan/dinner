# coding=utf-8
# __author__ = 'mic'

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.core import serializers
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.list import BaseListView

from .base_views import BaseLoginRequiredView



# MAIL_HOME = reverse('public:mail')
MAIL_HOME = ''

class MailView(BaseLoginRequiredView):

    def __init__(self):
        super(MailView, self).__init__()

    def get(self, request, tpl, mail_id):
        """"""
        var = {}

        return render(request, tpl, var)

    def post(self, request, tpl):
        email = request.POST.get('email')
        not_found = True if None else False
        if not_found:
            return HttpResponseRedirect(MAIL_HOME)

        else:
            # todo: i18n
            messages.add_message(request, messages.INFO, '无效的用户名或密码。')
            return render(request, tpl, {'email': email})