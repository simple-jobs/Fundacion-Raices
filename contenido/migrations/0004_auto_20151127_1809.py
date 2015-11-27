# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0003_comunidades_fortalecimiento_modernizacion_paz'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Investigacione',
        ),
        migrations.AlterField(
            model_name='comunidades',
            name='descripcion',
            field=models.TextField(max_length=1000, verbose_name=b'Comunidades y Medio Ambiente Sostenible'),
        ),
        migrations.AlterField(
            model_name='fortalecimiento',
            name='descripcion',
            field=models.TextField(max_length=1000, verbose_name=b'Fortalecimiento Institucional'),
        ),
        migrations.AlterField(
            model_name='modernizacion',
            name='descripcion',
            field=models.TextField(max_length=1000, verbose_name=b'Modernizacion de Gobiernos Locales'),
        ),
        migrations.AlterField(
            model_name='paz',
            name='descripcion',
            field=models.TextField(max_length=1000, verbose_name=b'Paz, Seguridad y Postconflicto'),
        ),
    ]
