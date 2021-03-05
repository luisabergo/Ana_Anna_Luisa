# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0002_auto_20210202_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
