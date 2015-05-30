# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20150528_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=b'200'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='fullname',
            field=models.CharField(max_length=b'200', null=True),
        ),
    ]
