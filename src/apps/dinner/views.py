# from django.shortcuts import render
from src.apps import *

# Create your views here.

def index(request, tpl):
  var = {
    'foo': range(0, 3),
    'bar': range(0,5)
  }
  return render(request, tpl, var)
