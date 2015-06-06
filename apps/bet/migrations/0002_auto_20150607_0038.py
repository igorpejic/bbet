# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='songs',
            field=models.ManyToManyField(related_name='artist', to='bet.Song'),
        ),
    ]
