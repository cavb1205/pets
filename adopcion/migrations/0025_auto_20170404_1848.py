# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-04 18:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0024_auto_20170404_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id_categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adopcion.CategoriaPost', verbose_name='Categoria de la Historia'),
        ),
    ]
