# coding=utf-8

from django.db import models
from public.models import User
from public.models import Calendar


class Provider(models.Model):
    """供应商"""
    name = models.CharField(max_length=50)
    location = models.CharField('位置', max_length=200, null=True)
    telephone = models.CharField('手机', max_length=30, null=True)
    phone = models.CharField('固话', max_length=30, null=True)
    manager = models.ForeignKey(User, null=True)
    url = models.URLField('链接地址', null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


# class MenuType(models.Model):
#     """菜单类别"""


class MenuItem(models.Model):
    """菜单条目"""
    provider = models.ForeignKey(Provider, verbose_name='供应商', null=True)
    code = models.IntegerField('编码', blank=False, null=False)
    name = models.CharField('名称', max_length=30, default=None)
    # type = models.ForeignKey(MenuType)
    # 0=不辣, 1=微辣, 2=中辣, 3=重辣,
    hot_index = models.SmallIntegerField('辣度指数', default=0)
    # 0=普通, 1=特色菜
    is_special = models.SmallIntegerField('特色菜')
    unit = models.CharField('度量单位', max_length=30, default=u'例')
    normal_price = models.SmallIntegerField('正价')
    vip_price = models.SmallIntegerField('VIP会员价格')

    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s:%s-%s' % (self.provider, self.code, self.name)


# todo: 暂支持是否报名晚餐
class Order(models.Model):
    """晚餐报名表"""
    calendar = models.ForeignKey(Calendar)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s: %s' % (self.calendar.get_full_datetime(), self.user.username)


# todo: 将来支持点条目,以Top10为最终结果
class OrderItem(models.Model):
    """某日某人订某菜表"""
    calendar = models.ForeignKey(Calendar)
    user = models.ForeignKey(User)
    # order = models.ForeignKey(Order)
    item = models.ForeignKey(MenuItem)
    created_at = models.DateTimeField(auto_now_add=True)


class CalendarProvider(models.Model):
    """餐厅配置"""
    calendar = models.ForeignKey(Calendar)
    provider = models.ForeignKey(Provider)

    def __unicode__(self):
        return '%s: %s' % (self.calendar, self.provider.name)
