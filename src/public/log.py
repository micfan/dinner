# coding=utf-8
__author__ = 'mic'

from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.urlresolvers import reverse
# from public.models import FEException
#
#
#
class FEErrorCollectView(View):
    """前端异常"""

    def __init__(self):
        super(View, self).__init__()

    def get(self, request, tpl):
        """收集异常"""
        ex = FEException(
          message=request.GET.get('message')
        )
        if request.user.is_authenticated():
            ex.user = request.user
        ex.save()


        return HttpResponse('')
