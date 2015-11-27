# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0002_auto_20151126_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagene',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255, verbose_name=b'Titulo de la imagen')),
                ('descripcion', models.CharField(max_length=255, verbose_name=b'Descripcion de la imagen')),
                ('imagen', models.ImageField(upload_to=b'imagenes/', null=True, verbose_name=b'Imagen para galeria', blank=True)),
            ],
        ),
    ]
