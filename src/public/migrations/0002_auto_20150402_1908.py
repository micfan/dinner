# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='org',
            name='manager',
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.IntegerField(default=1, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='hired_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='idcard_no',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='org',
            field=models.ForeignKey(to='public.Org', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='qq',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='quited',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='conf',
            name='content',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='telephone',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
