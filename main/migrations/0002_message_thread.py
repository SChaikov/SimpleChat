# Generated by Django 4.0.5 on 2022-06-07 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
                ('thread', models.CharField(max_length=255)),
                ('created', models.CharField(max_length=255)),
                ('is_read', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participants', models.CharField(max_length=255)),
                ('created', models.CharField(max_length=255)),
                ('updated', models.CharField(max_length=255)),
            ],
        ),
    ]
