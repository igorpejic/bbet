# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0003_auto_20150607_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='bet_type',
            field=models.CharField(default=b'3', max_length=20, choices=[(b'1', b'Top 10'), (b'2', b'Top 20'), (b'3', b'1x2')]),
        ),
    ]
