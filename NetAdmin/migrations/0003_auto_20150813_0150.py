# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetAdmin', '0002_auto_20150807_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='reply_to',
            field=models.CharField(default='admin', max_length=200, blank=True),
            preserve_default=False,
        ),
    ]
