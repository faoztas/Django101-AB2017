# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_app', '0004_auto_20170205_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='kisi',
            name='eposta',
            field=models.EmailField(default='faoztas@gmail.com', max_length=254),
        ),
        migrations.AlterModelTable(
            name='kisi',
            table='kisi_tablosu',
        ),
    ]
