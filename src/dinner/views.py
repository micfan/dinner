# coding=utf-8

import datetime
import calendar

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required

from dinner.models import Order, CalendarProvider
from public.models import Calendar
from misc.views import JsonResult


class IndexView(View):
    """晚餐预定"""
    def __init__(self):
        super(IndexView, self).__init__()
        self.now = datetime.datetime.now()
        self.deadline_hour = 15  # 15:00 截止
        self.deadline_curr_text = u'已截止' if self.now.hour >= self.deadline_hour else u'进行中'
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

    # todo: 类内修饰器
    # @login_required
    def get(self, request, tpl):
        this_month_cals = Calendar.objects.filter(year=2015, month=self.now.month).extra(
          select={
              'has_booked': "select count(*) from dinner_order \
                            where dinner_order.calendar_id = public_calendar.id \
                            and dinner_order.user_id = 1"
          }
        )
        if not this_month_cals.exists():
            raise Exception('日历配置错误')
        # 计算空缺
        c = calendar.monthcalendar(self.now.year, self.now.month)
        first_week, last_week = c[0], c[len(c)-1]
        frirst_week_place_holder = 7 - len(set(first_week) - {0})

        var = {
            'order_count': Order.objects.filter(calendar__id=self.curr_cal.id).count(),
            'curr_cal': self.curr_cal,
            'curr_now': self.now,
            'deadline_hour': self.deadline_hour,
            'deadline_curr_text': self.deadline_curr_text,
            'curr_provider': self.curr_provider,
            'this_month_cals': this_month_cals,
            'frirst_week_place_holder': range(frirst_week_place_holder)
        }
        if self.curr_cal:
            o = Order.objects.filter(calendar=self.curr_cal).annotate(Count('user_id'))
            var['order_count'] = o[0].user_id__count if o.count() == 1 else 0
            var['is_holiday'] = self.curr_cal.is_holiday
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
                    # todo: API参数合法性检查, 如：是否假日、是过去日前点: def is_avilable_calendar(y, m, d, cal_id=0);
                    cal = Calendar.objects.get(id=cal_id, is_holiday=False)

                    # 过去的某天
                    if datetime.datetime(cal.year, month=cal.month, day=cal.day) <\
                        datetime.datetime(self.now.year, month=self.now.month, day=self.now.day):
                        return HttpResponse(j.error(3).json(), 'application/json')

                    # 今天截止时间
                    if cal.id == self.curr_cal.id and self.now.hour >= self.deadline_hour:
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


