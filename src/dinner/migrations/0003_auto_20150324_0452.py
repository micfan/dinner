# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dinner', '0002_auto_20150324_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='url',
            field=models.URLField(default=b'javascript:void(0);', verbose_name=b'\xe9\x93\xbe\xe6\x8e\xa5\xe5\x9c\xb0\xe5\x9d\x80'),
            preserve_default=True,
        ),
    ]
