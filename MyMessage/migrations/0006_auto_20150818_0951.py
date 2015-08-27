# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyMessage', '0005_auto_20150818_0927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='from_admin',
        ),
        migrations.RemoveField(
            model_name='conversation',
            name='from_parents',
        ),
        migrations.RemoveField(
            model_name='conversation',
            name='from_student',
        ),
        migrations.RemoveField(
            model_name='conversation',
            name='from_ta',
        ),
        migrations.RemoveField(
            model_name='conversation',
            name='to_admin',
        ),
        migrations.RemoveField(
            model_name='conversation',
            name='to_student',
        ),
        migrations.RemoveField(
            model_name='conversation',
            name='to_ta',
        ),
        migrations.AddField(
            model_name='conversation',
            name='type',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
