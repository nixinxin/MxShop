# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='code',
            field=models.CharField(max_length=4, verbose_name='验证码'),
        ),
    ]
