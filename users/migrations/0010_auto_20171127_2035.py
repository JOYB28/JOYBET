# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20171127_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='users.Match'),
        ),
        migrations.AlterField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='users.Team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='users.Team'),
        ),
    ]
