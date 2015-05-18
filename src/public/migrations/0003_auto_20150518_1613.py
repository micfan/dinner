# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_auto_20150510_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='married',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='calendar',
            name='is_holiday',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe8\x8a\x82\xe5\x81\x87\xe6\x97\xa5'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, null=True, verbose_name=b'public email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='private_email',
            field=models.EmailField(max_length=255, unique=True, null=True, verbose_name=b'private email'),
            preserve_default=True,
        ),
    ]
