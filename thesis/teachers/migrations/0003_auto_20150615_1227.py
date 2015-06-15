# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20150520_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchunit',
            name='description',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='bio',
            field=models.CharField(max_length=3000),
        ),
    ]
