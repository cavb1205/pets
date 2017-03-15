# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 18:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adopcion', '0009_eventos_id_estadoevento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adopcion',
            name='usuarioAdopcion',
        ),
        migrations.RemoveField(
            model_name='eventos',
            name='id_usuario',
        ),
        migrations.RemoveField(
            model_name='post',
            name='id_usuario',
        ),
        migrations.AddField(
            model_name='adopcion',
            name='UserAdopcion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eventos',
            name='id_User',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='id_User',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comedog',
            name='responsableComedog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
