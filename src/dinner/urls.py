from django.conf.urls import patterns, url, include

from dinner import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), {'tpl': 'dinner/index.html'}, name='index'),
)