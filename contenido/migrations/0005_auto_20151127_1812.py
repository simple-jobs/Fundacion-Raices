# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0004_auto_20151127_1809'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comunidades',
            new_name='Comunidade',
        ),
    ]
