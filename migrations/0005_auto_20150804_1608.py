# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0004_auto_20150804_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='img_block',
        ),
        migrations.RemoveField(
            model_name='image',
            name='img_small',
        ),
    ]
