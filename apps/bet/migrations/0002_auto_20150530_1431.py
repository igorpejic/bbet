# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('has_won', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to='bet.Better')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.SmallIntegerField()),
                ('song', models.ForeignKey(to='bet.Song')),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('songs', models.ManyToManyField(to='bet.Song', through='bet.Position')),
            ],
        ),
        migrations.RemoveField(
            model_name='betting',
            name='user',
        ),
        migrations.AlterField(
            model_name='listofbets',
            name='bet_id',
            field=models.ForeignKey(to='bet.Bet'),
        ),
        migrations.DeleteModel(
            name='Betting',
        ),
        migrations.AddField(
            model_name='position',
            name='week',
            field=models.ForeignKey(to='bet.Week'),
        ),
    ]
