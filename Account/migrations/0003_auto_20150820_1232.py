# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20150806_0845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('new_message_from_agent', models.IntegerField(null=True)),
                ('new_message_from_student', models.IntegerField(null=True)),
                ('new_message_from_parents', models.IntegerField(null=True)),
                ('new_message_from_TA', models.IntegerField(null=True)),
                ('new_essays', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='avatar',
            field=models.FileField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='account',
            name='phone',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
