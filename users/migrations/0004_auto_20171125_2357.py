# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171125_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='match_round',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='title',
            field=models.CharField(default='match', max_length=50),
        ),
    ]