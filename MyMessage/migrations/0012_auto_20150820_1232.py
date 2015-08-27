# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyMessage', '0011_conversation_newest_reply_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='Messages',
        ),
        migrations.AddField(
            model_name='conversation',
            name='messages',
            field=models.ManyToManyField(to='MyMessage.Message'),
        ),
    ]
