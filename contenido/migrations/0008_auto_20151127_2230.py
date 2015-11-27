# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0007_auto_20151127_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagene',
            name='descripcion',
            field=models.TextField(max_length=1000, verbose_name=b'Descripcion de la imagen'),
        ),
    ]
