# Generated by Django 4.0.5 on 2022-06-07 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_thread_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='participants',
        ),
    ]
