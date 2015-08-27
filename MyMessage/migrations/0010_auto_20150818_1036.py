# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyMessage', '0009_auto_20150818_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='p1',
            new_name='receiver',
        ),
        migrations.RenameField(
            model_name='conversation',
            old_name='p2',
            new_name='sender',
        ),
        migrations.RemoveField(
            model_name='conversation',
            name='starter',
        ),
    ]
