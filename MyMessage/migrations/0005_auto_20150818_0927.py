# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyMessage', '0004_auto_20150818_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='to_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='conversation',
            name='to_student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='conversation',
            name='to_ta',
            field=models.BooleanField(default=False),
        ),
    ]
