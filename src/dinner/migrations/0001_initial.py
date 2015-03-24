# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarProvider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField(verbose_name=b'\xe7\xbc\x96\xe7\xa0\x81')),
                ('hot_index', models.SmallIntegerField(default=0, verbose_name=b'\xe8\xbe\xa3\xe5\xba\xa6\xe6\x8c\x87\xe6\x95\xb0')),
                ('is_special', models.SmallIntegerField(verbose_name=b'\xe7\x89\xb9\xe8\x89\xb2\xe8\x8f\x9c')),
                ('unit', models.CharField(default='\u4f8b', max_length=30, verbose_name=b'\xe5\xba\xa6\xe9\x87\x8f\xe5\x8d\x95\xe4\xbd\x8d')),
                ('normal_price', models.SmallIntegerField(verbose_name=b'\xe6\xad\xa3\xe4\xbb\xb7')),
                ('vip_price', models.SmallIntegerField(verbose_name=b'VIP\xe4\xbc\x9a\xe5\x91\x98\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=200, verbose_name=b'\xe4\xbd\x8d\xe7\xbd\xae')),
                ('telephone', models.CharField(max_length=30, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba')),
                ('phone', models.CharField(max_length=30, verbose_name=b'\xe5\x9b\xba\xe8\xaf\x9d')),
                ('url', models.URLField(default=b'javascript:void(0);', verbose_name=b'\xe9\x93\xbe\xe6\x8e\xa5\xe5\x9c\xb0\xe5\x9d\x80')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
