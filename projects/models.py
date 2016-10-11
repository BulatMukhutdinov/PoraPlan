from __future__ import unicode_literals
from django.db import models
from authorization.models import UserProfile


class ProjectStatus(models.Model):
    Name = models.CharField(max_length=50)


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField(null=True)
    status = models.ForeignKey(ProjectStatus, on_delete=models.PROTECT,null=True)


class ProjectRoles(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)


class TeamMembers(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    member = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    role = models.ForeignKey(ProjectRoles, on_delete=models.PROTECT)
