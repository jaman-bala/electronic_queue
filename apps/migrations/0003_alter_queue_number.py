# Generated by Django 4.2.4 on 2023-08-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_operator_is_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='number',
            field=models.IntegerField(unique=True),
        ),
    ]
