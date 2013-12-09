# coding=utf-8
# __author__ = 'mic'
from public.models import User

class ModelEmailBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            return user
        except User.DoesNotExist:
            return None
