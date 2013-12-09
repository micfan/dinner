# coding=utf-8
from django.conf.urls import patterns, url, include
from django.conf import settings

from public import views, signup, profile, log, message, uploads

urlpatterns = patterns('public.views',
    url(r'^$', 'index', {'tpl': 'public/index.html'}, name='index'),


    # HTML
    url(r'^h/(?P<tpl_prefix>\w*)', 'html'),
)

urlpatterns += patterns('',

    # 登录
    url(r'^%s$' % settings.LOGIN_URL[1:], views.LoginView.as_view(), {'tpl': 'public/login.html'}, name='login'),
    # 登出
    url(r'^%s$' % settings.LOGOUT_URL[1:], 'public.views.logout'),
    # 注册
    url(r'^signup/$', signup.SignupView.as_view(), {'tpl': 'public/signup.html'}),

    # 重置密码
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset',
        {
        'template_name': 'public/password_reset_form.html',
        'email_template_name': 'public/password_reset_email.html',
        'subject_template_name': 'registration/password_reset_subject.txt'},
        name='password_reset',),

    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', {'template_name': 'public/password_reset_done.html'}, name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'django.contrib.auth.views.password_reset_confirm', {'template_name': 'public/password_reset_confirm.html'}, name='password_reset_confirm'),

    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', {'template_name': 'public/password_reset_complete.html'}, name='password_reset_complete'),

    # todo: 泛username类型URL。无法区别常规URL与username based URL, 故仅去掉斜杠以区分正则
    # url(r'^(?P<username>\w+)$', views.ProfileView.as_view(), {'tpl': 'public/profile.html'}),
    url(r'^profile/$', views.ProfileView.as_view(), {'tpl': 'public/profile.html'}, name='profile'),
    url(r'^message/(?P<mail_id>.+)?/?$', message.MessageView.as_view(), {'tpl': 'public/message/index.html'}, name='message'),
    url(r'^upload/$', uploads.UploadView.as_view(), {'tpl': 'public/upload.html'}, name='upload'),

    url(r'^api/', include('apis.urls'), name='apis'),
    url(r'^oauth2/', include('apps.oauth2.urls'), name='apps'),
)

urlpatterns += patterns('',
    url(r'^fe-error-report/$', log.FEErrorCollectView.as_view(), name='fe_report_url'),
)