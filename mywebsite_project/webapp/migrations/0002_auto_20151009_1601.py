# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='img_large_name',
            field=models.CharField(default=b'', max_length=32),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='img_small_name',
            field=models.CharField(default=b'', max_length=32),
            preserve_default=True,
        ),
    ]
