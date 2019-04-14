# -*- coding: utf-8 -*-
"""
"""

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework_extensions.routers import NestedRouterMixin

from tasks import views


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


# Create a router and register our viewsets with it.
router = NestedDefaultRouter()

tasks_router = router.register('tasks', views.TaskViewSet)
tasks_router.register(
    'attachments', views.FileViewSet,
    base_name='tasks-attachments',
    parents_query_lookups=['task']
)

router.register(r'users', views.UserViewSet)
router.register(r'files', views.FileViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
