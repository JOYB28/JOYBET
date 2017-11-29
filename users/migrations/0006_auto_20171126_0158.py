# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_comment_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='last_recharge',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='users.Match'),
        ),
    ]