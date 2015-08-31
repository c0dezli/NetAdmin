# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0007_account_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='sex',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='account',
            name='whatsup',
            field=models.TextField(null=True),
        ),
    ]
