# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-24 05:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=250)),
                ('video_file', models.FileField(upload_to=b'')),
            ],
        ),
    ]
