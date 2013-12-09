# coding=utf-8
# Initial table

from public.models import Calendar
from dinner.models import Provider, CalendarProvider
from django.core.management import BaseCommand


def init_calendar():
    """初始化日历"""
    year, month = 2015, 12
    # 31天
    big_month = (1, 3, 5, 7, 8, 10, 12)
    Feb = 2
    for m in xrange(1, month+1):
        if m == Feb:
            day = 29
        elif m in big_month:
            day = 32
        else:
            day = 31

        for d in xrange(1, day):
            # todo: 如何判断星期几？第几周？
            Calendar.objects.get_or_create(year=year, month=m, day=d)


def init_provider():
    providers = [
        {'name': '有滋有味(宝山)', 'location': '上海宝山区水产路709号', 'phone': '5656 0792'}
    ]
    for p in providers:
        Provider.objects.get_or_create(name=p.get('name'), location=p.get('location'), telephone=p.get('telephone'),
                                       phone=p.get('phone'), url=p.get('url'))


def init_calendar_provider():
    """初始化每日餐厅配置: 3，4月"""
    cals = Calendar.objects.filter(year=2015, month__in=(3, 4))
    try:
        provider = Provider.objects.get(name='有滋有味(宝山)')
        for c in cals:
            CalendarProvider.objects.get_or_create(calendar=c, provider=provider)
    except Provider.DoesNotExist:
        # 重新配置
        main()


def main():
    """初始化数据"""
    init_calendar()
    init_provider()
    init_calendar_provider()



class Command(BaseCommand):
    """命令"""
    def handle(self, *args, **options):
        print '-'*80
        main()