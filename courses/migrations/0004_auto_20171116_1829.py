# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-17 02:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_random'),
    ]

    operations = [
        migrations.RenameField(
            model_name='step',
            old_name='course',
            new_name='course1',
        ),
    ]
