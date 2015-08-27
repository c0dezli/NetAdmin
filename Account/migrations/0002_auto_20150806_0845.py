# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='my_child',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='my_parents',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='my_student',
            field=models.TextField(default=b'[]', null=True),
        ),
    ]
