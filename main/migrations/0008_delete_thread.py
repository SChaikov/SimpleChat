# Generated by Django 4.0.5 on 2022-06-08 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_thread_participants'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Thread',
        ),
    ]
