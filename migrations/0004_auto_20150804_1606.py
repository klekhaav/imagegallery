# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import image.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_image_original_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='img_block',
            field=models.ImageField(default=datetime.datetime(2015, 8, 4, 16, 6, 8, 133629, tzinfo=utc), upload_to=image.models.dir_name),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='img_small',
            field=models.ImageField(default=datetime.datetime(2015, 8, 4, 16, 6, 29, 424798, tzinfo=utc), upload_to=image.models.dir_name),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='original_img',
            field=models.ImageField(upload_to=image.models.dir_name),
        ),
    ]
