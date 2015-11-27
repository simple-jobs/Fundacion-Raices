# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0006_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='archivo',
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion',
            field=models.TextField(max_length=25000, verbose_name=b'Descripcion del proyecto'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name=b'Nombre del proyecto'),
        ),
    ]
