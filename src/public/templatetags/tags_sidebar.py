# coding=utf-8
# __author__ = 'mic'

import datetime
from django import template

register = template.Library()

# @register.simple_tag
# def current_time(format_string):
#     return datetime.datetime.now().strftime(format_string)

@register.simple_tag(takes_context=True)
def active_sidebar(context, path):
    """高亮当前sidebar-item"""
    curr_path = context['request'].path
    return ' active ' if path in curr_path else ' '