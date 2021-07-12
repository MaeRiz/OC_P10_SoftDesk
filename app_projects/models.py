from django.db import models
from django.conf import settings


class Contributors(models.Model):
    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_id = models.IntegerField()
    permission = models.Choices()
    role = models.CharField(max_length=128, blank=False)


class Projects(models.Model):
    project_id = models.IntegerField()
    title = models.CharField(max_length=128, blank=False)
    description = models.TextField(max_length=2048, blank=False)
    type = models.CharField(max_length=128, blank=False)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Issues(models.Model):
    title = models.CharField(max_length=128, blank=False)
    desc = models.TextField(max_length=2048, blank=False)
    tag = models.CharField(max_length=128, blank=False)
    priority = models.CharField(max_length=128, blank=False)
    project_id = models.ForeignKey()
    status = models.CharField(max_length=128, blank=False)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assignee_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL)
    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    comment_id = models.IntegerField()
    description = models.TextField(max_length=2048)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue_id = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)