# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('desc', models.CharField(max_length=50, verbose_name=b'\xe9\x85\x8d\xe7\xbd\xae\xe8\xaf\xb4\xe6\x98\x8e')),
                ('content', models.CharField(max_length=50, verbose_name=b'\xe9\x85\x8d\xe7\xbd\xae\xe8\xaf\xb4\xe6\x98\x8e')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
