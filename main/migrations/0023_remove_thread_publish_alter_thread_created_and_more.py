# Generated by Django 4.0.5 on 2022-06-09 12:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_thread_publish_alter_thread_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='publish',
        ),
        migrations.AlterField(
            model_name='thread',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='thread',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
