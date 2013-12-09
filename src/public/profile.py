# coding=utf-8
# __author__ = 'mic'

import json
from django.core import serializers
from django.db import models
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .base_views import BaseLoginRequiredView
from . import uploads


# todo: 学signup，建表单
class PasswordView(BaseLoginRequiredView):

    def __init__(self):
        super(PasswordView, self).__init__()

    def get(self, request, tpl):
        """"""
        # todo: login_require()
        # if not request.user.is_authenticated():
        #     login_url = reverse('public:login')
        #     return HttpResponseRedirect(login_url)
        # else:
        return render(request, tpl, {})

    def post(self, request, tpl):
        user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(self.next_url)
        else:
            # todo: i18n
            messages.add_message(request, messages.INFO, '无效的用户名或密码。')
            return render(request, tpl)


class ProfileView(BaseLoginRequiredView):

    def __init__(self):
        super(ProfileView, self).__init__()

    def get(self, request, tpl):
        """"""
        var = {}

        return render(request, tpl, var)

    def post(self, request, tpl):
        user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(self.next_url)
        else:
            # todo: i18n
            messages.add_message(request, messages.INFO, '无效的用户名或密码。')
            return render(request, tpl)


class AvatarView(BaseLoginRequiredView):

    def __init__(self):
        super(AvatarView, self).__init__()

    def post(self, request, *args, **kwargs):
        response = uploads.UploadView.as_view()(self.request)
        j = json.loads(response.getvalue())
        # TODO: JsonResult.parse(j)
        media_filepath = j.get('data').get('media_filepath')
        request.user.avatar = media_filepath
        request.user.save()
        return HttpResponseRedirect(reverse('public:profile'))
