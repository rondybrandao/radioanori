# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radiosite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagem',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.CharField(choices=[('policial', 'Policial'), ('politica', 'Politica'), ('cultura', 'Cultura'), ('esporte', 'Esporte'), ('cotidiano', 'Cotidiano')], default='SOME STRING', max_length=10),
        ),
    ]
