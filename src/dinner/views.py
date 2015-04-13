# coding=utf-8

import datetime
import calendar
import json
import time

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required

from dinner.models import Order, CalendarProvider
from public.models import Calendar, Conf
from misc.views import JsonResult


class IndexView(View):
    """晚餐预定"""
    def __init__(self):
        super(IndexView, self).__init__()
        self.now = datetime.datetime.now()


        try:
            deadline_time_str = Conf.objects.get(name='book_end_time')
            _deadline_time = datetime.datetime.strptime(deadline_time_str.content, '%H:%M')
            self.deadline_datetime = datetime.datetime(year=self.now.year, month=self.now.month, day=self.now.day,
                                                   hour=_deadline_time.hour, minute=_deadline_time.minute)
        except Conf.DoesNotExist:
            raise Exception('截止时间配置错误')

        self.deadline_curr_text = u'已截止' if self.now >= self.deadline_datetime else u'进行中'
        Calendars = Calendar.objects.filter(year=self.now.year, month=self.now.month, day=self.now.day)
        if Calendars.count() == 1:
            self.curr_cal = Calendars[0]
            cp = CalendarProvider.objects.filter(calendar=self.curr_cal)
            if cp.count() == 1:
                self.curr_provider = cp[0].provider
            else:
                self.curr_provider = None
                raise Exception(u"日历-供应商配置错误")
        else:
            self.curr_cal = None
            self.curr_provider = None
            raise Exception(u"日历配置错误")

        self.order_count = Order.objects.filter(calendar__id=self.curr_cal.id).count()

    # todo: 类内修饰器
    # @login_required
    def get(self, request, tpl):
        if request.user.is_authenticated():
            select = {
              'has_booked': ("select count(*) from dinner_order \
                            where dinner_order.calendar_id = public_calendar.id \
                            and dinner_order.user_id = %d" % request.user.id)
            }
        else:
            select = {"has_booked": 0}
        this_month_cals = Calendar.objects.filter(year=2015, month=self.now.month).extra(select=select
            ).order_by('day')
        if not this_month_cals.exists():
            raise Exception('日历配置错误')
        # 计算空缺
        c = calendar.monthcalendar(self.now.year, self.now.month)
        first_week, last_week = c[0], c[len(c)-1]
        frirst_week_place_holder = 7 - len(set(first_week) - {0})

        var = {
            'order_count': self.order_count,
            'curr_cal': self.curr_cal,
            'curr_now': self.now,
            'deadline_datetime': self.deadline_datetime,
            'deadline_curr_text': self.deadline_curr_text,
            'curr_provider': self.curr_provider,
            'this_month_cals': this_month_cals,
            'frirst_week_place_holder': range(frirst_week_place_holder)
        }

        return render(request, tpl, var)

    # todo: 修饰器
    # todo: 扩充接口参数改为y, m, d, 以便外部API调用
    def post(self, request, tpl):
        """API: 订阅接口
        :return JsonResult {}
        """
        j = JsonResult(message='预定成功', data=0)
        if not request.user.is_authenticated():
            return HttpResponse(j.error(4).json(), 'application/json')

        cal_id = request.POST.get('cal_id')
        has_booked = request.POST.get('has_booked')

        if cal_id and has_booked:
            try:
                has_booked = (int(has_booked) == 1)
                # UI显示已预定，则后端取消；反之亦然
                if has_booked:
                    Order.objects.filter(calendar__id=cal_id, user=request.user).delete()
                    j.message = '该日晚餐预定已取消'
                else:
                    # todo: API: def is_avilable_calendar(y, m, d, cal_id=0);
                    cal = Calendar.objects.get(id=cal_id, is_holiday=False)

                    # 过去的某天
                    if datetime.datetime(cal.year, month=cal.month, day=cal.day) <\
                        datetime.datetime(self.now.year, month=self.now.month, day=self.now.day):
                        return HttpResponse(j.error(3).json(), 'application/json')

                    # 今天截止时间
                    if cal.id == self.curr_cal.id and self.now.time() >= self.deadline_datetime.time():
                        return HttpResponse(j.error(5).json(), 'application/json')

                    # 不用get_or_create()导致sqlite3 database clocked
                    if not Order.objects.filter(calendar=cal, user=request.user).exists():
                        Order.objects.create(calendar=cal, user=request.user)
                # 今日已预定数量
                j.data = Order.objects.filter(calendar__id=self.curr_cal.id).count()
            except Calendar.DoesNotExist:
                j.error(3)
        else:
            j.error(3)
        return HttpResponse(j.json(), 'application/json')


class OrderView(View):
    def __init__(self):
        super(OrderView, self).__init__()
        d = IndexView()
        self.curr_cal = d.curr_cal
        self.order_count = d.order_count


    # todo: 做页面，加参数format=json来格式化接口
    def get(self, request, tpl):
        """API: 今天已预定人数"""
        j = JsonResult()
        o = Order.objects.filter(calendar__id=self.curr_cal.id).extra(select={
          'cn_name': "select cn_name from public_user where public_user.id = dinner_order.user_id",
          'username': "select username from public_user where public_user.id = dinner_order.user_id"
        }).order_by('username')
        j.message = o.count()
        order_users = o.values_list('cn_name', flat=True)
        order_users = [u.encode('utf-8') for u in order_users if u]
        j.data = order_users

        format = request.GET.get('f')
        if format == 'json':
            return HttpResponse(j.json(), 'application/json')
        else:
            var = {
                'j': j.dict(),
                'curr_cal': self.curr_cal,
                'order_count': self.order_count
            }
            return render(request, tpl, var)


