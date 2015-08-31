# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_account_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='whatsup',
            field=models.TextField(default='hey!!'),
            preserve_default=False,
        ),
    ]
