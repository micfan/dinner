# coding=utf-8
__author__ = 'mic'

from django import forms


from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render

from public.forms import UserSignupForm






def signup(request, tpl):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/books/")
    else:
        form = UserSignupForm()
    return render(request, tpl, {'form': form})
