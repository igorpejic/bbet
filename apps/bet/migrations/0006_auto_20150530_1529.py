# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0005_auto_20150530_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collaboration',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='collaboration',
            name='song',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='last_name',
        ),
        migrations.AddField(
            model_name='artist',
            name='songs',
            field=models.ManyToManyField(to='bet.Song'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.DeleteModel(
            name='Collaboration',
        ),
    ]
