from rest_framework import serializers
from .models import Comment, Contributor, Issue, Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['title', 'description', 'type', 'author_user_id']
        read_only_fields = ['author_user_id']



class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        exclude = ['project']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'