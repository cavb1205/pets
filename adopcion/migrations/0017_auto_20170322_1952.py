# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0016_auto_20170322_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='fecha_cumpleanos',
            field=models.DateField(blank=True, null=True),
        ),
    ]
