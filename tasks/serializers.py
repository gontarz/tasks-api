# -*- coding: utf-8 -*-
"""
"""

from rest_framework import serializers
from django.contrib.auth.models import User
from tasks.models import Task, File


class FileSerializer(serializers.HyperlinkedModelSerializer):
    # task = serializers.HyperlinkedRelatedField(view_name='file-detail', read_only=True)

    name = serializers.ReadOnlyField()

    class Meta():
        model = File
        fields = ('id', 'file', 'name', 'created', 'task')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    attachments = serializers.HyperlinkedRelatedField(many=True, view_name='file-detail', read_only=True)
    creator = serializers.HyperlinkedRelatedField(view_name='task-detail', read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'content', 'owner', 'creator', 'created', 'updated', 'attachments')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks_creator = serializers.HyperlinkedRelatedField(many=True, view_name='task-detail', read_only=True)
    tasks_owner = serializers.HyperlinkedRelatedField(many=True, view_name='task-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'tasks_creator', 'tasks_owner')
