# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_auto_20150820_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='notification',
            field=models.ForeignKey(default=1, to='Account.Notification'),
            preserve_default=False,
        ),
    ]
