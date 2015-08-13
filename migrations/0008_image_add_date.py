# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0007_auto_20150806_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 16, 54, 0, 688400, tzinfo=utc), verbose_name=b'add date'),
            preserve_default=False,
        ),
    ]
