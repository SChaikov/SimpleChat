# Generated by Django 4.0.5 on 2022-06-08 14:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_thread_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 14, 19, 50, 724866, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 8, 14, 19, 50, 712864, tzinfo=utc)),
        ),
    ]
