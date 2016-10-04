from __future__ import unicode_literals
from django.db import models
from projects.models import Project


class Agenda(models.Model):
    date_time = models.DateTimeField()


class AgendaDetail(models.Model):
    meeting = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    topic = models.TextField()
    time_allocated = int
    priority = int
    summary = models.TextField()
    conclusion = models.TextField()
    summary = models.TextField()


class AgendaAction(models.Model):
    agenda_detail = models.ForeignKey(AgendaDetail, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    deadline = models.DateField()


class Meeting(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    topic = models.CharField(max_length=250)
    date = models.DateTimeField()
    agenda = models.OneToOneField(Agenda, on_delete=None)

