# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0007_auto_20150530_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre', models.ForeignKey(to='bet.Song')),
            ],
        ),
        migrations.AlterField(
            model_name='listofbet',
            name='data',
            field=models.CharField(max_length=20, choices=[(b'1', b'Will rise'), (b'x', b'Will stay'), (b'2', b'Will fall')]),
        ),
    ]
