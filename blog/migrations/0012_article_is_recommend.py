# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170728_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_recommend',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u63a8\u8350'),
        ),
    ]
