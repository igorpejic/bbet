# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0004_auto_20150530_1452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collaboration',
            old_name='artist_id',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='listofbet',
            old_name='bet_id',
            new_name='bet',
        ),
        migrations.AlterField(
            model_name='song',
            name='youTube_link',
            field=models.URLField(null=True, blank=True),
        ),
    ]
