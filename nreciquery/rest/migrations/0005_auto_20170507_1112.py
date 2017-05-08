# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0004_auto_20170506_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='ingredient_names', to='rest.Ingredient'),
        ),
    ]
