# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0007_adopcion_id_ciudadadopcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='comedog',
            name='id_ciudadComedog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adopcion.Ciudad'),
        ),
        migrations.AddField(
            model_name='eventos',
            name='id_ciudadEvento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adopcion.Ciudad'),
        ),
    ]