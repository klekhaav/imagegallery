# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image.models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0006_auto_20150806_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_width',
        ),
        migrations.AlterField(
            model_name='image',
            name='original_img',
            field=models.ImageField(upload_to=image.models.dir_name),
        ),
    ]
