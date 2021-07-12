from django.db import models
from django.conf import settings

PRIORITY_CHOICES = [
    ('FAIBLE', 'FAIBLE'),
    ('MOYENNE', 'MOYENNE'),
    ('ELEVEE', 'ELEVEE'),
]
STATS_CHOICES = [
    ('A FAIRE', 'A FAIRE'),
    ('EN COURS', 'EN COURS'),
    ('TERMINE', 'TERMINE'),
]
TAG_CHOICES = [
    ('BUG', 'BUG'),
    ('AMELIORATION', 'AMELIORATION'),
    ('TACHE', 'TACHE'),
]

class Contributors(models.Model):
    user_id = models.IntegerField()
    project_id = models.IntegerField()
    permission = models.Choices()
    role = models.CharField(max_length=128)


class Projects(models.Model):
    project_id = models.IntegerField()
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    type = models.CharField(max_length=128)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Issues(models.Model):
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=2048)
    tag = models.CharField(choices=TAG_CHOICES, max_length=100)
    priority = models.CharField(choices=PRIORITY_CHOICES, default='MOYENNE', max_length=100)
    project_id = models.IntegerField()
    status = models.CharField(choices=STATS_CHOICES, default='A FAIRE', max_length=100)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assignee_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL)
    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    comment_id = models.IntegerField()
    description = models.CharField(max_length=2048)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue_id = models.ForeignKey()
    created_time = models.DateTimeField(auto_now_add=True)