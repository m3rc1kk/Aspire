# Generated by Django 5.1.1 on 2024-09-25 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(max_length=100),
        ),
    ]
