# coding=utf8

try: import simplejson as json
except: import json
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

def login(request, tpl):
  """"""
  a = {'a': 'ad'}
  return render_to_response(tpl, a)
  # js = {'status': 1, 'message': 'ok', 'ec': 0}
  # return HttpResponse(content=json.dumps(js), status=200, content_type='application/json')

@login_required
def logout(request):
  """"""
  js = {'status': 1, 'message': 'ok', 'ec': 0}
  return HttpResponse(content=json.dumps(js), status=200, content_type='application/json')

def html(request, tpl_prefix):
  tpl = 'html/%s.html' % tpl_prefix
  return render(request, tpl)
