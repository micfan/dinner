# coding=utf-8
from django.conf.urls import patterns, url, include
from django.conf import settings

from public import views, signup

urlpatterns = patterns('public.views',
    url(r'^$', 'index', {'tpl': 'public/index.html'}),

    url(r'^%s$' % settings.LOGOUT_URL[1:], 'logout'),

    # HTML
    url(r'^h/(?P<tpl_prefix>\w*)', 'html'),
)

urlpatterns += patterns('',
    # 登录
    url(r'^%s$' % settings.LOGIN_URL[1:], views.LoginView.as_view(), {'tpl': 'public/login.html'}),
    url(r'^signup/$', signup.SignupView.as_view(), {'tpl': 'public/signup.html'}),
)

# urlpatterns += patterns('public.signup',
#
# )