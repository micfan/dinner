# coding=utf-8
# Initial table

from public.models import Calender
from dinner.models import Provider, CalenderProvider
from django.core.management import BaseCommand

# todo: 初始化数据
def foo():
    print 'foo'


class Command(BaseCommand):
    """命令"""
    def handle(self, *args, **options):
        print '-'*80
        foo()