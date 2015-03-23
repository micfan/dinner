# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('dinner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='provider',
            field=models.ForeignKey(verbose_name=b'\xe4\xbe\x9b\xe5\xba\x94\xe5\x95\x86', to='dinner.Provider', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='manager',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
