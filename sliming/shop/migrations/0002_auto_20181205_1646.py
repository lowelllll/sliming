# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-05 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='offline',
            field=models.ManyToManyField(null=True, to='shop.OfflineShop'),
        ),
    ]
