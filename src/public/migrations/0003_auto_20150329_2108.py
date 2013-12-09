# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_conf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cn_name',
            field=models.CharField(max_length=100, unique=True, null=True, db_index=True),
            preserve_default=True,
        ),
    ]
