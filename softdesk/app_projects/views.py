from django.db.models.deletion import RestrictedError
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Comment, Contributor, Issue, Project
from .serializers import CommentSerializer, IssueSerializer, ProjectSerializer, ContributorsSerializer


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        projects_ids_lst = []
        for object in Contributor.objects.filter(user_id=self.request.user):
            projects_ids_lst.append(object.project_id)
        return Project.objects.filter(id__in=projects_ids_lst)

    def create(self, request):

        data = request.data.copy()
        data['author'] = request.user.id
        serialized_data = ProjectSerializer(data=data)
        serialized_data.is_valid(raise_exception=True)
        project = serialized_data.save()

        contributor = Contributor.objects.create(
            user= request.user,
            project= project,
            permission= '',
            role= 'AUTHOR',
        )
        contributor.save()

        return Response(serialized_data.data, status=status.HTTP_201_CREATED)


class ContributorsViewset(viewsets.ModelViewSet):

    serializer_class = ContributorsSerializer

    def get_queryset(self):
        return Contributor.objects.filter(project_id=self.kwargs['project_pk'])

    def create(self, request, project_pk=None):

        data = request.data.copy()
        contributors_lst = []

        for object in Contributor.objects.filter(project_id=project_pk):
            contributors_lst.append(object.user_id)

        if int(data['user']) in contributors_lst:
            return Response('User already added.', status=status.HTTP_400_BAD_REQUEST)

        else:
            data['project'] = project_pk
            data['role'] = 'CONTRIBUTOR'
            serialized_data = ContributorsSerializer(data=data)
            serialized_data.is_valid(raise_exception=True)
            serialized_data.save()

            return Response(serialized_data.data, status=status.HTTP_201_CREATED)


class IssueViewSet(viewsets.ModelViewSet):

    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs['project_pk'])

    def create(self, request, project_pk=None):

        data = request.data.copy()
        data['author'] = request.user.pk
        data['project'] = project_pk
        serialized_data = IssueSerializer(data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()

        return Response(serialized_data.data, status=status.HTTP_201_CREATED)

class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs['issue_pk'])

    def create(self, request, project_pk=None, issue_pk=None):
        data = request.data.copy()
        data['author'] = request.user.pk
        data['issue'] = issue_pk
        serialized_data = CommentSerializer(data=data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)
