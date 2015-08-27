# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyMessage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('starter', models.CharField(max_length=200)),
                ('replier', models.CharField(max_length=200)),
                ('from_ta', models.BooleanField(default=False)),
                ('from_student', models.BooleanField(default=False)),
                ('from_admin', models.BooleanField(default=False)),
                ('from_parents', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='first_message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='from_admin',
        ),
        migrations.RemoveField(
            model_name='message',
            name='from_parents',
        ),
        migrations.RemoveField(
            model_name='message',
            name='from_student',
        ),
        migrations.RemoveField(
            model_name='message',
            name='from_ta',
        ),
        migrations.RemoveField(
            model_name='message',
            name='reply_to',
        ),
        migrations.AddField(
            model_name='conversation',
            name='Messages',
            field=models.ForeignKey(to='MyMessage.Message'),
        ),
    ]
