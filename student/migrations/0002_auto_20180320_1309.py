# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-20 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('reviews', models.TextField()),
                ('fees', models.IntegerField()),
                ('exam', models.CharField(max_length=255)),
                ('score', models.IntegerField()),
                ('specialisation', models.TextField()),
                ('location', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
