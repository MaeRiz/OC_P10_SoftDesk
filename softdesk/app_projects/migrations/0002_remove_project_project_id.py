# Generated by Django 3.2.5 on 2021-08-12 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_id',
        ),
    ]
