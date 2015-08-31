# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_account_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='school',
            field=models.CharField(default='Berkely', max_length=40),
            preserve_default=False,
        ),
    ]
