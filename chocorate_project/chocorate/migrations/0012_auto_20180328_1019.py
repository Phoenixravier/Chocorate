# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-28 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chocorate', '0011_remove_userprofile_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chocolate',
            name='picture_url',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]