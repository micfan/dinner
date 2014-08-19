from django.conf.urls import patterns, url, include

urlpatterns = patterns('src.apps.dinner.views',
  url(r'^$', 'index', {'tpl': 'dinner/index.html'}),
)

urlpatterns += patterns('src.apps.dinner.apis', 
  url(r'book$', 'book'),
)