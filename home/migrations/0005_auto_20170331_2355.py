# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 23:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170331_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='image',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]