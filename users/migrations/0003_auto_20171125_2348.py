# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171125_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='away_team_score',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team_score',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
