# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dinner', '0003_auto_20150325_0044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calendarprovider',
            old_name='Calendar',
            new_name='calendar',
        ),
    ]
