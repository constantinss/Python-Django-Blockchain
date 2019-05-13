# Generated by Django 2.1.7 on 2019-03-18 12:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0002_auto_20190315_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 18, 12, 50, 28, 875456, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 18, 12, 50, 28, 875539, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 18, 12, 50, 28, 876080, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 18, 12, 50, 28, 876163, tzinfo=utc)),
        ),
    ]
