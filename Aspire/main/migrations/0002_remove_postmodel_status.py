# Generated by Django 5.1.1 on 2024-09-18 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='status',
        ),
    ]
