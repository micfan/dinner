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
        this_month_cals = Calendar.objects.filter(year=2015, month=self.now.month)
        if not this_month_cals.exists():
            raise Exception('日历配置错误')
        var = {
            'col': range(0, 1),
            'row': range(0, 5),
            'order_count': Order.objects.filter(calendar__id=self.curr_cal.id).count(),
            'curr_cal': self.curr_cal,
            'deadline': self.deadline,
            'deadline_curr_text': self.deadline_curr_text,
            'curr_provider': self.curr_provider,
            'this_month_cals': this_month_cals
        }
        if self.curr_cal:
            o = Order.objects.filter(calendar=self.curr_cal).annotate(Count('user_id'))
            var['order_count'] = o[0].user_id__count if o.count() == 1 else 0
            var['is_holiday'] = self.curr_cal.is_holiday
        return render(request, tpl, var)

    # todo: 修饰器
    # todo: 扩充接口参数改为y, m, d
    def post(self, request, tpl):
        cal_id = request.POST.get('cal_id')
        selected = request.POST.get('selected')
        j = JsonResult(message='预定成功', data=0)
        if not request.user.is_authenticated():
            return HttpResponse(j.error(4).json(), 'application/json')
        if cal_id and selected:
            try:
                unselected = (int(selected) == 0)
                if unselected:
                    Order.objects.filter(calendar__id=cal_id, user=request.user).delete()
                    j.message = '该日晚餐预定已取消'
                else:
                    # todo: 参数合法性检查, 如：是否假日、是过去日前点: def is_avilable_calendar(y, m, d, cal_id=0);
                    cal = Calendar.objects.get(id=cal_id, is_holiday=False)
                    order, created = Order.objects.get_or_create(calendar=cal, user=request.user)
                    # 今日已预定数量
                    j.data = Order.objects.filter(calendar__id=self.curr_cal.id).count()
            except Calendar.DoesNotExist:
                j.error(3)
        else:
            j.error(3)
        return HttpResponse(j.json(), 'application/json')


