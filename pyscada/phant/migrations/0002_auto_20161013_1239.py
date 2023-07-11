# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 12:39
from __future__ import unicode_literals

from django.db import migrations, models
import pyscada.phant.models


class Migration(migrations.Migration):
    dependencies = [
        ("phant", "0002_auto_20161012_2017"),
    ]

    operations = [
        migrations.AlterField(
            model_name="phantdevice",
            name="private_key",
            field=models.CharField(
                default=pyscada.phant.models.gen_random_key, max_length=20
            ),
        ),
        migrations.AlterField(
            model_name="phantdevice",
            name="public_key",
            field=models.SlugField(
                default=pyscada.phant.models.gen_random_key, max_length=20, unique=True
            ),
        ),
    ]
