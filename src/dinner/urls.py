from django.conf.urls import patterns, url, include

import views

urlpatterns = patterns('dinner.apis',
    url(r'book$', 'book'),
)

urlpatterns += patterns('',
    url(r'^$', views.IndexView.as_view(), {'tpl': 'dinner/index.html'}, name='index'),
)