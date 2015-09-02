# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyMessage', '0012_auto_20150820_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='addfile',
            field=models.FileField(default=1, upload_to=b''),
            preserve_default=False,
        ),
    ]
