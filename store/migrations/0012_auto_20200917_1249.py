# Generated by Django 2.0.2 on 2020-09-17 06:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_bloglist_specialist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloglist',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 17, 12, 49, 42, 903416)),
        ),
    ]
