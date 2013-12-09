# coding=utf8
from django.shortcuts import render
from django.http import HttpResponse
try:
  import simplejson as json
except:
  import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response


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
