# Generated by Django 3.0.2 on 2020-01-14 12:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 14, 12, 43, 31, 523946, tzinfo=utc), verbose_name='Date Published'),
            preserve_default=False,
        ),
    ]
