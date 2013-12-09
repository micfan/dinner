# coding=utf-8
__author__ = 'mic'

from django import forms


from django.http import HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render_to_response, render
from django.core.urlresolvers import reverse
from django.contrib.auth import login
from django.contrib.auth import authenticate

from public.forms import UserSignupForm


class SignupView(View):
    """注册"""

    def get(self, request, tpl):
        form = UserSignupForm()
        return render(request, tpl, {'form': form})

    def post(self, request, tpl):
        form = UserSignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            curr_user = authenticate(username=request.POST.get('username'), password=request.POST.get('password1'))
            login(request, curr_user)

            return HttpResponseRedirect(reverse('dinner:index'))
        return render(request, tpl, {'form': form})


