from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView

from meetings.models import Meeting, Agenda, MeetingType
from django.core.urlresolvers import reverse_lazy

from projects.models import Project


class MeetingList(ListView):
    model = Meeting


class MeetingCreate(TemplateView):
    template_name = "meetings/new_meeting.html"
    for e in Project.objects.all():
        print(e)

    def get_context_data(self, **kwargs):
        context = super(MeetingCreate, self).get_context_data(**kwargs)
        context['meetingTypes'] = MeetingType.objects.all()
        context['projects'] = Project.objects.all()
        return context


class MeetingUpdate(UpdateView):
    model = Meeting
    success_url = reverse_lazy('meeting_list')
    fields = ['topic', 'project', 'date']


class MeetingDelete(DeleteView):
    model = Meeting
    success_url = reverse_lazy('metting_list')


class AgendaList(ListView):
    model = Agenda


class AgendaCreate(CreateView):
    model = Agenda
    success_url = reverse_lazy('agenda_list')
    fields = ['date_time', 'time_keeper', 'facilitator']


class AgendaUpdate(UpdateView):
    model = Agenda
    success_url = reverse_lazy('agenda_list')
    fields = ['date_time']


class AgendaDelete(DeleteView):
    model = Agenda
    success_url = reverse_lazy('agenda_list')
