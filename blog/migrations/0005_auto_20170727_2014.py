# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170727_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='img_url',
        ),
        migrations.AddField(
            model_name='ad',
            name='image_url',
            field=models.CharField(default='/static/images/a2.jpg', max_length=100),
        ),
    ]