# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_room_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='total_viewers',
            field=models.CharField(max_length=200),
        ),
    ]
