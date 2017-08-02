# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-20 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('radiosite', '0017_auto_20170617_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', verbose_name='Attachment')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radiosite.Anuncio')),
            ],
        ),
    ]
