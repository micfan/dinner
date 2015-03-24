# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('username', models.CharField(unique=True, max_length=100, db_index=True)),
                ('first_name', models.CharField(unique=True, max_length=100, db_index=True)),
                ('last_name', models.CharField(unique=True, max_length=100, db_index=True)),
                ('cn_name', models.CharField(unique=True, max_length=100, db_index=True)),
                ('avatar', models.URLField(blank=True)),
                ('telephone', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.SmallIntegerField(verbose_name=b'\xe5\xb9\xb4')),
                ('month', models.SmallIntegerField(verbose_name=b'\xe6\x9c\x88')),
                ('day', models.SmallIntegerField(verbose_name=b'\xe6\x97\xa5')),
                ('is_holiday', models.SmallIntegerField(default=0, verbose_name=b'\xe6\x98\xaf\xe8\x8a\x82\xe5\x81\x87\xe6\x97\xa5')),
                ('holiday_mark', models.CharField(max_length=50, verbose_name=b'\xe8\x8a\x82\xe5\x81\x87\xe6\x97\xa5\xe8\xaf\xb4\xe6\x98\x8e')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
