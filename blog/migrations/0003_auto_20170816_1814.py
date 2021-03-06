# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-16 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_quote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='content',
            new_name='text',
        ),
        migrations.AddField(
            model_name='quote',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
