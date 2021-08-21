from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Comment, Contributor, Issue, Project
from .serializers import CommentSerializer, IssueSerializer, ProjectSerializer



class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    #permission_classes = (IsAuthenticated,)

    #def create(request):


class IssueViewSet(viewsets.ModelViewSet):

    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_pk'])

class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs['issue_pk'])