# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_auto_20150615_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='research_unit',
        ),
        migrations.AddField(
            model_name='researchunit',
            name='teacher',
            field=models.ForeignKey(blank=True, to='teachers.Teacher', null=True),
        ),
    ]
