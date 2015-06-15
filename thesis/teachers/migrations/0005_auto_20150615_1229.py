# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_auto_20150615_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchunit',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
