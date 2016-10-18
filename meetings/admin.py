from django.contrib import admin
from meetings.models import *

admin.site.register(Meeting)
admin.site.register(MeetingRoles)
admin.site.register(MeetingType)
admin.site.register(MeetingParticipators)
admin.site.register(Agenda)
admin.site.register(AgendaDetail)
admin.site.register(AgendaAction)
