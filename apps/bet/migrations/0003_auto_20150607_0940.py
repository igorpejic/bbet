# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0002_auto_20150607_0038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listofbet',
            old_name='data',
            new_name='choice',
        ),
    ]
