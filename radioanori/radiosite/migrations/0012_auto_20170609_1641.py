# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-09 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radiosite', '0011_anuncio_imagem_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='image',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='imagem_1',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
