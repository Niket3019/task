# Generated by Django 5.0 on 2023-12-31 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_assignee'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
