# coding=utf8

try:
    import simplejson as json
except ImportError:
    import json
from django.core import serializers
from django.db import models
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe


def index(request, tpl):
    """Home page"""

    return render(request, tpl, {})
    # return HttpResponse(content='Hello, world!', status=200, content_type='text/html')

from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


class LoginView(View):

    def __init__(self):
        super(LoginView, self).__init__()
        self.next_url = reverse('dinner:index')
        self.deadline = 15  # 15:00

    def get(self, request, tpl):
        """"""
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.next_url)
        else:
            var = {
                'deadline': '15:00',
            }

            return render(request, tpl, var)
        # js = {'status': 1, 'message': 'ok', 'ec': 0}
        # return HttpResponse(content=json.dumps(js), status=200, content_type='application/json')

    def post(self, request, tpl):
        user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(self.next_url)
        else:
            # todo: i18n
            messages.add_message(request, messages.INFO, '无效的用户名或密码。')
            return render(request, tpl)

from django.contrib.auth.views import logout as django_logout
# todo: 用class based view实现吧
@login_required
def logout(request):

    if request.method == 'GET':
        next_page = request.GET.get('next')
        if not next_page:
            next_page = '/'
        # todo: 登出用户
        return django_logout(request, next_page)
    if request.method == 'POST':
        js = {'status': 1, 'message': 'ok', 'ec': 0}
        return HttpResponse(content=json.dumps(js), status=200, content_type='application/json')


def html(request, tpl_prefix):
    tpl = 'html/%s.html' % tpl_prefix
    return render(request, tpl)
