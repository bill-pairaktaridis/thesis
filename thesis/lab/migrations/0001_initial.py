# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=100)),
                ('research_objects', models.CharField(max_length=500)),
                ('services', models.CharField(max_length=500)),
                ('essay', models.CharField(max_length=2000)),
            ],
        ),
    ]
