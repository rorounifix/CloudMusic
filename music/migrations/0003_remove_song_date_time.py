# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-21 10:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='date_time',
        ),
    ]
