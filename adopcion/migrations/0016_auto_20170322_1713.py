# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0015_perfil_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='videoPost',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagenPost',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/post/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slugPost',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
