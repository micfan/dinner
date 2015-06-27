# coding=utf-8
# __author__ = 'mic'
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from django.core.urlresolvers import reverse

# login_url = reverse('public:login')

class BaseLoginRequiredView(View):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(BaseLoginRequiredView, cls).as_view(**initkwargs)
        return login_required(view)
