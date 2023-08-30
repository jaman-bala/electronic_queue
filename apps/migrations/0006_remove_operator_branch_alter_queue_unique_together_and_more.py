# Generated by Django 4.2.4 on 2023-08-30 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_branch_remove_operator_is_main_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operator',
            name='branch',
        ),
        migrations.AlterUniqueTogether(
            name='queue',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='queue',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='queue',
            name='operator',
        ),
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.DeleteModel(
            name='Operator',
        ),
        migrations.DeleteModel(
            name='Queue',
        ),
    ]
