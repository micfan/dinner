from django.conf.urls import patterns, url, include
from django.conf import settings

from public import views

urlpatterns = patterns('public.views',
    url(r'^$', 'index', {'tpl': 'public/index.html'}),

    url(r'^%s$' % settings.LOGOUT_URL[1:], 'logout'),

    # pure html pages
    url(r'^h/(?P<tpl_prefix>\w*)', 'html'),
)

urlpatterns += patterns('',
  url(r'^%s$' % settings.LOGIN_URL[1:], views.LoginView.as_view(), {'tpl': 'public/login.html'}),
)