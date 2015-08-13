# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='with_us',
            field=models.DateField(default=datetime.datetime(2015, 8, 3, 13, 41, 23, 165727, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
