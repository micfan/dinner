# coding=utf-8

import datetime

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
        self.deadline = 15  # 15:00
        self.deadline_curr_text = u'已截止' if self.now.hour >= self.deadline else u'进行中'
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
        var = {
            'foo': range(0, 3),
            'bar': range(0, 5),
            'order_count': 0,
            'curr_cal': self.curr_cal,
            'deadline': self.deadline,
            'deadline_curr_text': self.deadline_curr_text,
            'curr_provider': self.curr_provider
        }

        if self.curr_cal:
            o = Order.objects.filter(calendar=self.curr_cal).annotate(Count('user_id'))
            var['order_count'] = o[0].user_id__count if o.count() == 1 else 0
            var['is_holiday'] = self.curr_cal.is_holiday
        return render(request, tpl, var)

    # todo: 修饰器
    def post(self, request, tpl):
        cal_id = request.POST.get('cal_id')
        j = JsonResult(message='预定成功')
        try:
            cal = Calendar.objects.get(id=cal_id)
            # Order.objects.get_or_create(calendar=cal, user=request.user)
            j.error(3)
        except Calendar.DoesNotExist:
            j.error(3)
        return HttpResponse(j.json(), 'application/json')


