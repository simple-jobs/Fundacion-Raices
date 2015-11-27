# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0002_auto_20151126_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comunidades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(max_length=1000, verbose_name=b'Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Fortalecimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(max_length=1000, verbose_name=b'Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Modernizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(max_length=1000, verbose_name=b'Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Paz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(max_length=1000, verbose_name=b'Descripcion')),
            ],
        ),
    ]
