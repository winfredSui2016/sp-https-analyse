# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='resources',
            fields=[
                ('ID', models.AutoField(serialize=False, primary_key=True)),
                ('URL', models.CharField(max_length=2000)),
                ('ParentURL', models.CharField(max_length=2000)),
                ('ResourceType', models.CharField(max_length=255)),
                ('Type', models.CharField(max_length=255)),
                ('Domain', models.CharField(max_length=2000)),
                ('IsHttps', models.CharField(max_length=4)),
                ('Time', models.TimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
