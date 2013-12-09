# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.SmallIntegerField(verbose_name=b'\xe5\xb9\xb4')),
                ('month', models.SmallIntegerField(verbose_name=b'\xe6\x9c\x88')),
                ('day', models.SmallIntegerField(verbose_name=b'\xe6\x97\xa5')),
                ('is_holiday', models.SmallIntegerField(default=0, verbose_name=b'\xe6\x98\xaf\xe8\x8a\x82\xe5\x81\x87\xe6\x97\xa5')),
                ('holiday_mark', models.CharField(max_length=50, verbose_name=b'\xe8\x8a\x82\xe5\x81\x87\xe6\x97\xa5\xe8\xaf\xb4\xe6\x98\x8e')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
