# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dinner', '0002_auto_20150325_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='location',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xe4\xbd\x8d\xe7\xbd\xae'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='phone',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe5\x9b\xba\xe8\xaf\x9d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='telephone',
            field=models.CharField(max_length=30, null=True, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='url',
            field=models.URLField(null=True, verbose_name=b'\xe9\x93\xbe\xe6\x8e\xa5\xe5\x9c\xb0\xe5\x9d\x80'),
            preserve_default=True,
        ),
    ]
