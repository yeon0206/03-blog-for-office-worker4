# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-11 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_auto_20170911_0355'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='subtitle',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
