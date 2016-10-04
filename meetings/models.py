from __future__ import unicode_literals
from django.db import models
from projects.models import Project


class Meeting(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
