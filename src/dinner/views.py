# coding=utf-8

from django.shortcuts import render



def index(request, tpl):
  var = {
    'foo': range(0, 3),
    'bar': range(0, 5)
  }
  return render(request, tpl, var)
