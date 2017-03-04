# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0003_auto_20170224_0300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adopcion',
            old_name='imagenAdopcion',
            new_name='imagenDestacadaAdopcion',
        ),
        migrations.AddField(
            model_name='adopcion',
            name='imagenAdopcion1',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/adopcion/'),
        ),
        migrations.AddField(
            model_name='adopcion',
            name='imagenAdopcion2',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/adopcion/'),
        ),
    ]
