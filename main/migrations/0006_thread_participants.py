# Generated by Django 4.0.5 on 2022-06-08 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_thread_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='participants',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
