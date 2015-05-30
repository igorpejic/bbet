# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0003_remove_better_for_week'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListOfBet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.CharField(max_length=20)),
                ('bet_id', models.ForeignKey(to='bet.Bet')),
                ('song', models.ForeignKey(to='bet.Song')),
            ],
        ),
        migrations.RemoveField(
            model_name='listofbets',
            name='bet_id',
        ),
        migrations.RemoveField(
            model_name='listofbets',
            name='song',
        ),
        migrations.DeleteModel(
            name='ListOfBets',
        ),
    ]
