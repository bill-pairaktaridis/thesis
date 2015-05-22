# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('rank', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=2000)),
                ('link', models.CharField(max_length=50)),
            ],
        ),
    ]
