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
from models import Message, User


# MAIL_HOME = reverse('public:message')
MAIL_HOME = ''

class MessageView(BaseLoginRequiredView):

    def __init__(self):
        super(MessageView, self).__init__()

    def get(self, request, tpl, mail_id):
        """"""
        var = {
            'messages': request.user.get_unread_messages()
            # 'messages': [
            #     {'content': 'hello, world!'},
            #     {'content': 'hello, world!'},
            #     {'content': 'hello, world!'}
            # ]
        }

        return render(request, tpl, var)

    def post(self, request, tpl):
        message = request.POST.get('content')
        to = request.POST.get('to')
        not_found = False if User.objects.filter(id=to) else True
        if not_found:
            return HttpResponse()

        else:
            # todo: i18n
            messages.add_message(request, messages.INFO, '无效的用户名或密码。')
            return render(request, tpl, {'email': email})