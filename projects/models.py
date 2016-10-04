from __future__ import unicode_literals
from django.db import models


class ProjectStatus(models.Model):
    Name = models.CharField(max_length=50)


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    status = models.ForeignKey(ProjectStatus, on_delete=None)
