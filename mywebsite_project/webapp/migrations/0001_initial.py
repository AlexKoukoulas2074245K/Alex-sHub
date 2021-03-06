# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('subheading', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=1024)),
                ('details', models.CharField(max_length=1024)),
                ('download_link', models.URLField(null=True)),
                ('github_link', models.URLField(null=True)),
                ('views', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
