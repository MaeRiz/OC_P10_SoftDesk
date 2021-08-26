# Generated by Django 3.2.5 on 2021-08-09 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(max_length=128)),
                ('role', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField()),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=2048)),
                ('type', models.CharField(max_length=128)),
                ('author_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('desc', models.TextField(max_length=2048)),
                ('tag', models.CharField(choices=[('BUG', 'BUG'), ('AMELIORATION', 'AMELIORATION'), ('TACHE', 'TACHE')], max_length=100)),
                ('priority', models.CharField(choices=[('FAIBLE', 'FAIBLE'), ('MOYENNE', 'MOYENNE'), ('ELEVEE', 'ELEVEE')], default='MOYENNE', max_length=100)),
                ('status', models.CharField(choices=[('A FAIRE', 'A FAIRE'), ('EN COURS', 'EN COURS'), ('TERMINE', 'TERMINE')], default='A FAIRE', max_length=100)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('assignee_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_projects.contributor')),
                ('author_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_projects.project')),
            ],
        ),
        migrations.AddField(
            model_name='contributor',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_projects.project'),
        ),
        migrations.AddField(
            model_name='contributor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=2048)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('author_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_projects.issue')),
            ],
        ),
    ]