# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 14:44
from __future__ import unicode_literals

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0020_auto_20170323_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenidoPost',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
