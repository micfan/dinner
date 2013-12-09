# coding=utf-8
# __author__ = 'mic'
import os
import uuid
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .base_views import BaseLoginRequiredView
from django.conf import settings

from misc.views import JsonResult


def make_uuid_filename(path, extension=''):
    name = str(uuid.uuid4())
    target_file = '.'.join([os.path.join(path, name), extension])
    if os.path.exists(target_file):
        target_file = make_uuid_filename(path)
    return target_file

def handle_uploaded_file(f, sub_dir=''):
    """
    sub_dir: sub path under settings.MEDIA_ROOT
    """
    target_path = settings.MEDIA_ROOT
    if sub_dir:
        sub_path = os.path.join(settings.MEDIA_ROOT, sub_dir)
        target_path = sub_path
        if not os.path.exists(sub_path) or not os.path.isdir(sub_path):
            os.mkdir(sub_path)

    # TODO: allowed_content_type = []
    # content_type = f.content_type
    # TODO: max_size = 1234
    # size = f._size

    if f._name.index('.') > -1:
        extension = f._name.split('.')[-1]
    else:
        extension = ''
    target_name = make_uuid_filename(target_path, extension)
    with open(target_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    media_filepath = os.path.join(sub_dir, os.path.basename(target_name))
    return media_filepath

class UploadView(BaseLoginRequiredView):
    def __init__(self):
        super(UploadView, self).__init__()

    def get(self, request, tpl):
        """A temp page to upload file """
        var = {}
        return render(request, tpl, var)

    def post(self, request,  *args, **kwargs):
        f = request.FILES['file']
        # TODO: file_url
        media_filepath = handle_uploaded_file(f)
        media_url = os.path.join(settings.MEDIA_URL, media_filepath)
        http_url = ''.join([request.scheme, '://', request.get_host(), media_url])
        j = JsonResult(data={
            'file_url': http_url,
            'media_filepath': media_filepath
        })
        return HttpResponse(j.json(), 'application/json')


