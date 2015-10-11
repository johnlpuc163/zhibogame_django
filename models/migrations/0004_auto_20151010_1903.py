# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_auto_20151010_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='platformgame',
            name='game',
            field=models.ForeignKey(default=1, to='models.Game'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platformgame',
            name='platform',
            field=models.ForeignKey(default=1, to='models.Platform'),
            preserve_default=False,
        ),
    ]
