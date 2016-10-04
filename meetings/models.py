from __future__ import unicode_literals
from django.db import models
from projects.models import Project


class Meeting(models):
    project = models.ManyToOneRel(Project, on_delete=models.CASCADE)
