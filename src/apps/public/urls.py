from django.conf.urls import patterns, url, include
from src.settings.base import LOGIN_URL, LOGOUT_URL

urlpatterns = patterns('src.apps.public.views',
  url(r'^$', 'index', {'tpl': 'public/index.html'}),
  url(r'^%s' % LOGIN_URL[1:], 'login', {'tpl': 'public/login.html'}),
  url(r'^%s' % LOGOUT_URL[1:], 'logout'),
  url(r'^h/(?P<tpl_prefix>\w*)', 'html'),
)