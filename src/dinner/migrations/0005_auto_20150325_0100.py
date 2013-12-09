# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dinner', '0004_auto_20150325_0056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Calendar',
            new_name='calendar',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='Calendar',
            new_name='calendar',
        ),
    ]
