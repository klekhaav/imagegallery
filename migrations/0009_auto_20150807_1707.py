# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0008_image_add_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='add_date',
        ),
        migrations.AddField(
            model_name='image',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 17, 7, 0, 189917, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
