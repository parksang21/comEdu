# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 07:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, default='', help_text='one word for title alias', unique=True, verbose_name='SLUG'),
        ),
    ]
