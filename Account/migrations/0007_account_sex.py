# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_account_whatsup'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='sex',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
