# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyMessage', '0003_auto_20150818_0810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='Messages',
        ),
        migrations.AddField(
            model_name='conversation',
            name='Messages',
            field=models.ManyToManyField(to='MyMessage.Message'),
        ),
    ]
