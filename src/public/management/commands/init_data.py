# coding=utf-8
# Initial table
import calendar
from public.models import Calendar
from dinner.models import Provider, CalendarProvider
from django.core.management import BaseCommand


def init_calendar():
    """初始化日历"""
    year, month = 2015, 12

    for m in range(1, month+1):
        c = calendar.monthcalendar(year, m)
        for week in c:
            for i, day in enumerate(week):
                # 也可用date模块计算
                if day != 0:
                    is_holiday = i in (5, 6)
                    if is_holiday:
                        holiday_mark = u'周末'
                    else:
                        holiday_mark = None
                    Calendar.objects.get_or_create(year=year, month=m, day=day, is_holiday=is_holiday,
                                                   holiday_mark=holiday_mark)


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
        print ('-'*80)
        main()