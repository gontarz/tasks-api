# -*- coding: utf-8 -*-
"""
"""

from rest_framework import permissions


class IsAdminOrOwnerOrCreatorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin and owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the task.
        return bool(
            obj.owner == request.user or
            obj.creator == request.user or
            request.user.is_staff
        )


class IsAdminOrUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin and owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return False
        # Write permissions are only allowed to the owner of the task.
        return bool(obj == request.user or request.user.is_staff)


from tasks.models import Task


class IsAdminOrOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admin and owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return bool(request.user.is_staff or obj.task in (Task.objects.filter(owner=request.user)))
