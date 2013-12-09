# coding=utf-8
__author__ = 'mic'


# todo:
def api_token_required(request):
    """跨域调用API, 传user_token标示, 实质还是session_id"""
    if not request.user.is_authenticated():
        return False
    if not request.POST.get('token'):
        return False
