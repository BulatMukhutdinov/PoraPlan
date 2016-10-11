from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from authorization.models import UserProfile


class ProjectRoles(models.Model):
    name = models.CharField(max_length=25)


class TeamMembers(models.Model):
    member = models.ForeignKey(User, on_delete=models.PROTECT)
    role = models.ForeignKey(ProjectRoles, on_delete=models.PROTECT)


class ProjectStatus(models.Model):
    Name = models.CharField(max_length=50)


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField(null=True)
    team_members =models.ManyToManyField(TeamMembers)
    team_users = models.ManyToManyField(User)
    status = models.ForeignKey(ProjectStatus, on_delete=models.PROTECT,null=True)
