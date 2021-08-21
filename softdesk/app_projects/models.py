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


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    type = models.CharField(max_length=128)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    permission = models.CharField(max_length=128)
    role = models.CharField(max_length=128)


class Issue(models.Model):
    title = models.CharField(max_length=128)
    desc = models.TextField(max_length=2048)
    tag = models.CharField(choices=TAG_CHOICES, max_length=100)
    priority = models.CharField(choices=PRIORITY_CHOICES, default='MOYENNE', max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(choices=STATS_CHOICES, default='A FAIRE', max_length=100)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assignee_user = models.ForeignKey(Contributor ,on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.CharField(max_length=2048)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)