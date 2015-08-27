# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetAdmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='first_message',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='message',
            name='reply_to',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='send_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
