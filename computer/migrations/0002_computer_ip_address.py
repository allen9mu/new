# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='IP_ADDRESS',
            field=models.CharField(default='0.0.0.0', max_length=20),
        ),
    ]
