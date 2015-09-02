# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0008_auto_20150830_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='for_user',
            field=models.CharField(default='admin', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notification',
            name='new_essays',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='notification',
            name='new_message_from_TA',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='notification',
            name='new_message_from_agent',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='notification',
            name='new_message_from_parents',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='notification',
            name='new_message_from_student',
            field=models.IntegerField(default=0),
        ),
    ]
