# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['week']},
        ),
        migrations.AlterModelOptions(
            name='week',
            options={'ordering': ['-date']},
        ),
    ]
