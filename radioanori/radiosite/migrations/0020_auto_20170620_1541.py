# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-20 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radiosite', '0019_auto_20170620_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(upload_to='attachments'),
        ),
    ]
