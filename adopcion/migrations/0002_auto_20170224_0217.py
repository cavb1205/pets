# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 02:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comedog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreComedog', models.CharField(max_length=100)),
                ('descripcionComedog', models.TextField()),
                ('ubicacionComedog', models.CharField(max_length=100)),
                ('imagenComedog', models.ImageField(upload_to='fotos/comedog/')),
                ('responsableComedog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adopcion.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEvento', models.CharField(max_length=100)),
                ('descripcionEvento', models.TextField()),
                ('fechaEvento', models.DateTimeField()),
                ('lugarEvento', models.CharField(max_length=100)),
                ('valorEvento', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fechaPubEvento', models.DateField(auto_now_add=True)),
                ('imagenEvento', models.ImageField(upload_to='fotos/eventos/')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adopcion.Usuario')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='contenidoPost',
            field=models.TextField(max_length=60000),
        ),
        migrations.AlterField(
            model_name='post',
            name='imagenPost',
            field=models.ImageField(upload_to='fotos/post/'),
        ),
    ]
