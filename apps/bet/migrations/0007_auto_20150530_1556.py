# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0006_auto_20150530_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listofbet',
            name='data',
            field=models.CharField(max_length=20, choices=[(b'1', b'up'), (b'X', b'stay'), (b'2', b'down')]),
        ),
    ]
