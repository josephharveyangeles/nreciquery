# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0005_auto_20170507_1112'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Condiment',
            new_name='Seasoning',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='condiments',
            new_name='seasonings',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='rest.Ingredient'),
        ),
    ]
