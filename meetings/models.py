from __future__ import unicode_literals
from django.db import models
from projects.models import Project
from projects.models import TeamMembers
from authorization.models import UserProfile


class MeetingType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class MeetingRoles(models.Model):
    type = models.ForeignKey(MeetingType, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=25)


class Agenda(models.Model):
    time = models.IntegerField(default=0)
    # meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, null=True)
    # time_keeper = models.ForeignKey(MeetingParticipators, related_name='time_keeper_user_profile',
    #                                 on_delete=models.PROTECT, null=True)
    # # facilitator = models.ForeignKey(MeetingParticipators, related_name='facilitator_user_profile',
    #                                 on_delete=models.PROTECT, null=True)
    # created_by = models.ForeignKey(UserProfile, on_delete=models.PROTECT, null=True)


class Topic(models.Model):
    name = models.CharField(max_length=100)
    agenda = models.ForeignKey(Agenda, on_delete=models.PROTECT, null=True)


class Meeting(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250, null=True)
    date = models.CharField(max_length=100, null=True)
    meeting_type = models.ForeignKey(MeetingType, on_delete=models.PROTECT, null=True)
    agenda = models.ForeignKey(Agenda, on_delete=models.PROTECT, null=True)
    relative_meeting = models.ForeignKey("self", null=True, default=None)

    def __str__(self):
        return self.name


class MeetingParticipators(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, null=True)
    participator = models.ForeignKey(TeamMembers, on_delete=models.PROTECT)
    role = models.ForeignKey(MeetingRoles, on_delete=models.PROTECT)
    rate = int


class AgendaDetail(models.Model):
    meeting = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    topic = models.TextField(null=True)
    time_allocated = int
    priority = int
    summary = models.TextField(null=True)
    conclusion = models.TextField(null=True)
    solution = models.TextField(null=True)
    presenter = models.ForeignKey(MeetingParticipators, on_delete=models.PROTECT, null=True)


class AgendaAction(models.Model):
    agenda_detail = models.ForeignKey(AgendaDetail, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    responsible = models.ForeignKey(MeetingParticipators, on_delete=models.PROTECT, null=True)
    deadline = models.DateField()
