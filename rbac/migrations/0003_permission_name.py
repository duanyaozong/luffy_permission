# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-12-21 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0002_auto_20191221_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='name',
            field=models.CharField(default='', max_length=32, verbose_name='url\u522b\u540d'),
        ),
    ]
