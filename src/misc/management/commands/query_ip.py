# coding=utf-8
# Initial table
import os
import string
import django
import json
import random
from celery import shared_task
from django.core.management import BaseCommand
from misc.management.commands.qqwry import get_qqwry


def query_ip(ip):
    """查询ip对应的地区，如上海市，江苏省
    :param ip {String}
    :return target_ip {Unicode}, area {Unicode}
    """
    target_ip = string.strip(ip)
    qqwry = get_qqwry()
    area, isp = qqwry.query(target_ip)
    area = unicode(area, "utf-8")
    print area
    print isp
    return target_ip, area, isp


# todo: Command Option参数 --ip=xxx
class Command(BaseCommand):
    """命令"""
    def handle(self, *args, **options):
        print '-'*80
        query_ip('101.93.22.196')