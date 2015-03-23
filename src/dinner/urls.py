from django.conf.urls import patterns, url, include

urlpatterns = patterns('dinner.views',
  url(r'^$', 'index', {'tpl': 'dinner/index.html'}),
)

urlpatterns += patterns('dinner.apis',
  url(r'book$', 'book'),
)