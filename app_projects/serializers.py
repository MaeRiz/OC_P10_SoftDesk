from rest_framework import serializers
from models import Contributors, Projects, Issues, Comments


class ProjectsSerializer(serializers.Serializer):
    
    def create(self, validated_data):
        return Projects.objects.create(**validated_data)

    def update(self):
        pass

    def delete(self):
        pass


class IssuesSerializer(serializers.Serializer):

    def create(self, validated_data):
        return Issues.objects.create(**validated_data)

    def update(self):
        pass
    
    def delete(self):
        pass


class CommentsSerializer(serializers.Serializer):

    def create(self, validated_data):
        return Comments.objects.create(**validated_data)

    def update(self):
        pass
    
    def delete(self):
        pass
