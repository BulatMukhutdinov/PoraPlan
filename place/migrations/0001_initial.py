# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 11:15
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('white_board', models.BooleanField()),
                ('black_board', models.BooleanField()),
                ('projector', models.BooleanField()),
                ('start_date', models.DateTimeField()),
                ('duration', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('num_of_persons', models.IntegerField()),
            ],
        ),
    ]
