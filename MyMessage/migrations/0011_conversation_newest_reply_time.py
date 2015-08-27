# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('MyMessage', '0010_auto_20150818_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='newest_reply_time',
            field=models.DateTimeField(default=datetime.datetime.utcnow(), auto_now=True),
            preserve_default=False,
        ),
    ]
