# coding=utf-8
# __author__ = 'mic'
# 用户相关tags, filters

from django import template

register = template.Library()

# @register.simple_tag
# def current_time(format_string):
#     return datetime.datetime.now().strftime(format_string)

@register.simple_tag(takes_context=True)
def has_unread_notifications(context):
    """您有未读消息"""
    has = context['request'].user.has_unread_mails()
    return ' has-unread-notifications ' if has == True else ' '
