# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20170331_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='image',
            field=models.FileField(blank=True, max_length=250, upload_to=''),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.FileField(blank=True, max_length=250, upload_to=''),
        ),
    ]