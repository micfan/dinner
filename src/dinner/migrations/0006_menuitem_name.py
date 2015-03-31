# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dinner', '0005_auto_20150325_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='name',
            field=models.CharField(default=None, max_length=30, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0'),
            preserve_default=True,
        ),
    ]
