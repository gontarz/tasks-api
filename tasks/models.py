from django.db import models

# Create your models here.

from django.db import models


class Task(models.Model):
    """
        Tasks model
    """
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()

    creator = models.ForeignKey('auth.User', related_name='tasks_creator', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='tasks_owner', on_delete=models.DO_NOTHING, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     super(Task, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created',)


class File(models.Model):
    """
    Files model
    """
    file = models.FileField(blank=False, null=False)
    name = models.CharField(max_length=256, null=True)

    task = models.ForeignKey('Task', related_name='attachments', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('task', 'file')
