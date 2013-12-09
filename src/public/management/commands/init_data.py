# coding=utf-8
# Initial table
import calendar
from public.models import Calendar
from public.models import Org, Conf
from dinner.models import CalendarProvider
from django.core.management import BaseCommand
import subprocess


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


# todo: 特殊节日设置
def init_special_holiday():
    sp = (
      # (2015, 4, 5, u'清明'),
    )
    for i in sp:
        y, m, d, mark = i[0], i[1], i[2], i[3]
        c = Calendar.objects.filter(year=y, month=m, day=d)
        c.update(holiday_mark=mark)


def init_provider():
    providers = [
        {'name': '有滋有味(宝山)', 'location': '上海宝山区水产路709号', 'phone': '5656 0792'}
    ]
    for p in providers:
        Org.objects.get_or_create(name=p.get('name'), location=p.get('location'), telephone=p.get('telephone'),
                                       phone=p.get('phone'), url=p.get('url'))


def init_calendar_provider():
    """初始化每日餐厅配置: 3，4月"""
    cals = Calendar.objects.filter(year=2015, month__in=(3, 4))
    try:
        provider = Org.objects.get(name='有滋有味(宝山)')
        for c in cals:
            CalendarProvider.objects.get_or_create(calendar=c, provider=provider)
    except Org.DoesNotExist:
        # 重新配置
        main()


# todo: 查询bower 配置.json文件参数
def init_bower_static():
    # subprocess.call(['bower', 'install'])
    pass


# todo: 初始化orgs，所有机构
def init_org():
    pass

# todo: 从文件初始化用户(username, email, org_code)
def init_user():
    pass


def init_conf():
    conf = (
      ('book_end_time', '11:30', '订餐截止时间'),
    )
    for c in conf:
        name, content, desc = c[0], c[1], c[2]
        Conf.objects.get_or_create(name=name, content=content, desc=desc)

def main():
    """初始化数据"""
    init_calendar()
    init_special_holiday()
    init_provider()
    init_calendar_provider()
    init_bower_static()
    init_conf()



class Command(BaseCommand):
    """命令"""
    def handle(self, *args, **options):
        print ('-'*80)
        main()