# from django.shortcuts import render

# Create your views here.

from rest_framework import permissions, viewsets

from rest_framework_extensions.mixins import NestedViewSetMixin

from django.contrib.auth.models import User

from tasks.models import Task, File
from tasks.serializers import TaskSerializer, UserSerializer, FileSerializer
from tasks.permissions import IsAdminOrOwnerOrCreatorOrReadOnly, IsAdminOrUserOrReadOnly, IsAdminOrOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (
        permissions.DjangoObjectPermissions & IsAdminOrUserOrReadOnly,
    )


class TaskViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (
        permissions.DjangoObjectPermissions & IsAdminOrOwnerOrCreatorOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class FileViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = File.objects.all()
    serializer_class = FileSerializer

    permission_classes = (
        permissions.DjangoObjectPermissions & IsAdminOrOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(name=self.request.FILES['file'].name)
