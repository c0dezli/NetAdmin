# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyMessage', '0008_auto_20150818_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='receiver',
            new_name='p1',
        ),
        migrations.RenameField(
            model_name='conversation',
            old_name='sender',
            new_name='p2',
        ),
        migrations.AddField(
            model_name='conversation',
            name='starter',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
