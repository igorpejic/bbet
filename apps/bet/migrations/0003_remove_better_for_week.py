# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bet', '0002_auto_20150530_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='better',
            name='for_week',
        ),
    ]
