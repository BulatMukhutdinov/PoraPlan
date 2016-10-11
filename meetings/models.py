from __future__ import unicode_literals
from django.db import models
from projects.models import Project
from projects.models import TeamMembers
from authorization.models import UserProfile


class MeetingType(models.Model):
    type = models.CharField(max_length=50)


class MeetingRoles(models.Model):
    type = models.ForeignKey(MeetingType, on_delete=models.PROTECT)
    name = models.CharField(max_length=25)


class Meeting(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    topic = models.CharField(max_length=250,null=True)
    date = models.DateTimeField(null=True)
    meeting_type = models.ForeignKey(MeetingType, on_delete=models.PROTECT)


class MeetingPatricipators(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    participator = models.ForeignKey(TeamMembers, on_delete=models.PROTECT)
    role = models.ForeignKey(MeetingRoles, on_delete=models.PROTECT)
    rate = int


class Agenda(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    date_time = models.DateTimeField(null=True)
    time_keeper = models.ForeignKey(MeetingPatricipators,related_name='time_keeper_user_profile',on_delete=models.PROTECT,null=True)
    facilitator = models.ForeignKey(MeetingPatricipators,related_name='facilitator_user_profile',on_delete=models.PROTECT,null=True)
    created_by = models.ForeignKey(UserProfile,on_delete=models.PROTECT,null=True)


class AgendaDetail(models.Model):
    meeting = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    topic = models.TextField(null=True)
    time_allocated = int
    priority = int
    summary = models.TextField(null=True)
    conclusion = models.TextField(null=True)
    solution = models.TextField(null=True)
    presenter = models.ForeignKey(MeetingPatricipators,on_delete=models.PROTECT)


class AgendaAction(models.Model):
    agenda_detail = models.ForeignKey(AgendaDetail, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    responsible = models.ForeignKey(MeetingPatricipators,on_delete=models.PROTECT)
    deadline = models.DateField()





