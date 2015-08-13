# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0005_auto_20150804_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_height',
            field=models.PositiveIntegerField(null=True, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='image',
            name='image_width',
            field=models.PositiveIntegerField(null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='original_img',
            field=models.ImageField(height_field=b'image_height', width_field=b'image_width', upload_to=b'dir_name'),
        ),
    ]
