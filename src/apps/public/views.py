from django.shortcuts import render
from django.http import HttpResponse
try:
  import simplejson as json
except:
  import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
@login_required
def index(request):
  """Home page"""

  return HttpResponse(content='Hello, world!', status=200, content_type='text/html')

def login(request, tpl):
  """"""
  a = {'a': 'ad'}
  return render_to_response(tpl, a)
  # js = {'status': 1, 'message': 'ok', 'ec': 0}
  # return HttpResponse(content=json.dumps(js), status=200, content_type='application/json')

def logout(request):
  """"""
  js = {'status': 1, 'message': 'ok', 'ec': 0}
  return HttpResponse(content=json.dumps(js), status=200, content_type='application/json')
