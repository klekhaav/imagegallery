# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_auto_20150803_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='original_img',
            field=models.FileField(default=datetime.datetime(2015, 8, 4, 12, 49, 1, 579234, tzinfo=utc), upload_to=b'user_media'),
            preserve_default=False,
        ),
    ]
