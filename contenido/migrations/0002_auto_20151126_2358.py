# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investigacione',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('presentacion', models.TextField(max_length=700, verbose_name=b'Introducion a la lineas de investigacion')),
                ('paz', models.TextField(max_length=700, verbose_name=b'Paz, Seguridad y Postconflicto')),
                ('comunidades', models.TextField(max_length=700, verbose_name=b'Comunidades y Medio Ambiente Sostenible')),
                ('fortalecimiento', models.TextField(max_length=700, verbose_name=b'Fortalecimiento Institucional')),
                ('modernizacion', models.TextField(max_length=700, verbose_name=b'Modernizacion de Gobiernos Locales')),
            ],
        ),
        migrations.DeleteModel(
            name='Investigacion',
        ),
        migrations.AlterField(
            model_name='contacto',
            name='correo',
            field=models.CharField(max_length=255, verbose_name=b'Correo de contacto'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='facebook',
            field=models.CharField(max_length=255, verbose_name=b'Link de facebook'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name=b'Nombre de contacto'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='telefono1',
            field=models.CharField(max_length=255, verbose_name=b'Telefono de contacto # 1'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='telefono2',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Telefono de contacto # 1', blank=True),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='twiter',
            field=models.CharField(max_length=255, verbose_name=b'Link de Twiter'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='archivo',
            field=models.FileField(null=True, upload_to=b'documentos/', blank=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name=b'Nombre del Documento'),
        ),
        migrations.AlterField(
            model_name='inicio',
            name='presentacion',
            field=models.TextField(max_length=700, verbose_name=b'Texto de Bienvenida'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion',
            field=models.TextField(max_length=700, verbose_name=b'Descripcion del proyecto'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name=b'Nombre del Proyecto'),
        ),
        migrations.AlterField(
            model_name='quienessomo',
            name='mision',
            field=models.TextField(max_length=700, verbose_name=b'Mision'),
        ),
        migrations.AlterField(
            model_name='quienessomo',
            name='objetivos',
            field=models.TextField(max_length=700, verbose_name=b'Objetivos'),
        ),
        migrations.AlterField(
            model_name='quienessomo',
            name='quienes_somos',
            field=models.TextField(max_length=700, verbose_name=b'Quienes Somos'),
        ),
        migrations.AlterField(
            model_name='quienessomo',
            name='vision',
            field=models.TextField(max_length=700, verbose_name=b'Vision'),
        ),
    ]
