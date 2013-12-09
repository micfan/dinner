# coding=utf-8
# Initial table
import datetime
import calendar

from django.core.management import BaseCommand
from django.conf import settings
from public.models import Calendar, User
from public.models import Org, Conf
from dinner.models import CalendarProvider

import subprocess
import csv

CURRENT_YEAR = datetime.datetime.now().year

def init_calendar():
    """初始化日历"""
    year, month = CURRENT_YEAR, 12

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
    cals = Calendar.objects.filter(year=2015, month__in=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    try:
        provider = Org.objects.get(name='宝升阁')
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


def init_user():
    user_file = settings.VAR_ROOT + '/user.csv'
    with open(user_file) as f:
        reader = csv.DictReader(f, delimiter=',')
        for r in reader:
            zname = r.get('zname')
            email = r.get('email')

            _pinyin = email.split('@') if email else []
            username = _pinyin[0] if len(_pinyin) == 2 else None

            gender = r.get('gender')
            telephone = r.get('mobile')
            idcard_no = r.get('idcard_no')
            quited = r.get('quited')
            user, created = User.objects.get_or_create(username=username, cn_name=zname, email=email, gender=gender, telephone=telephone,
                                       idcard_no=idcard_no, quited=quited)
            if created:
                user.set_password('123456')
                user.save()
                print r


def init_conf():
    conf = (
      ('book_end_time', '11:30', '订餐截止时间'),
    )
    for c in conf:
        name, content, desc = c[0], c[1], c[2]
        Conf.objects.get_or_create(name=name, content=content, desc=desc)


def init_site():
    """初始化站点表"""
    from django.contrib.sites.models import Site
    Site.objects.update(domain='dinner.micfan.com', name='生活@上海钢铁')


def main():
    """初始化数据"""
    # init_calendar()
    # init_special_holiday()
    # init_provider()
    init_calendar_provider()
    # init_bower_static()
    # init_conf()
    # init_org()
    # init_user()
    # init_site()



class Command(BaseCommand):
    """命令"""
    def handle(self, *args, **options):
        print ('-'*80)
        main()