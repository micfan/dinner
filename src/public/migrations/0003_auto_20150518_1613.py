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
