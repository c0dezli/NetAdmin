# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyMessage', '0002_auto_20150818_0807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='replier',
            new_name='receiver',
        ),
        migrations.RenameField(
            model_name='conversation',
            old_name='starter',
            new_name='sender',
        ),
        migrations.RemoveField(
            model_name='message',
            name='title',
        ),
    ]
