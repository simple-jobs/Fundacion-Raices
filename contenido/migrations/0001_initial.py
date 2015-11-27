# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255, verbose_name=b'Galeria')),
                ('correo', models.CharField(max_length=255, verbose_name=b'Galeria')),
                ('telefono1', models.CharField(max_length=255, verbose_name=b'Galeria')),
                ('telefono2', models.CharField(max_length=255, verbose_name=b'Galeria')),
                ('facebook', models.CharField(max_length=255, verbose_name=b'Galeria')),
                ('twiter', models.CharField(max_length=255, verbose_name=b'Galeria')),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255, verbose_name=b'Galeria')),
                ('archivo', models.FileField(null=True, upload_to=b'proyectos/', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('presentacion', models.TextField(max_length=700, verbose_name=b'Galeria')),
            ],
        ),
        migrations.CreateModel(
            name='Investigacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('presentacion', models.TextField(max_length=700, verbose_name=b'Galeria')),
                ('paz', models.TextField(max_length=700, verbose_name=b'Galeria')),
                ('comunidades', models.TextField(max_length=700, verbose_name=b'Galeria')),
                ('fortalecimiento', models.TextField(max_length=700, verbose_name=b'Galeria')),
                ('modernizacion', models.TextField(max_length=700, verbose_name=b'Galeria')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255, verbose_name=b'Galeria')),
                ('descripcion', models.TextField(max_length=700, verbose_name=b'Galeria')),
                ('archivo', models.FileField(null=True, upload_to=b'proyectos/', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuienesSomo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quienes_somos', models.TextField(max_length=700, verbose_name=b'Galeria')),
                ('mision', models.TextField(max_length=700, verbose_name=b'Galeria')),
                ('vision', models.TextField(max_length=700, verbose_name=b'Galeria')),
                ('objetivos', models.TextField(max_length=700, verbose_name=b'Galeria')),
            ],
        ),
    ]
