# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0021_auto_20170324_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenidoPost',
            field=models.TextField(max_length=60000),
        ),
    ]