# coding=utf-8
__author__ = 'mic'
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf.urls import patterns, url, include


from apis import urls as api_urls
from misc.views import JsonResult
# todo:
def api_token_required(request):
    """跨域调用API, 传access_token标示, 实质还是session_id"""
    if not request.user.is_authenticated():
        return False
    if not request.POST.get('access_token'):
        return False


def api_external(view_func):

    @csrf_exempt
    def django_view(request):
        params = {}
        try:
            body_params = json.loads(request.body) if request.body else {}
        except:
            body_params = {}
        params.update(body_params)

        try:
            result = view_func(**params)
            return HttpResponse(json.dumps(result, default=json_default), content_type="application/json")
        # todo: 自定义接口异常
        except Exception as err:
            return HttpResponse(err.data, status=err.status, content_type="application/json")

    api_urls.urlpatterns += patterns('', ('^%s/$'%view_func.__name__, django_view))
    return django_view
