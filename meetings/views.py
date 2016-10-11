from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from meetings.models import Meeting, Agenda
from django.core.urlresolvers import reverse_lazy


class MeetingList(ListView):
    model = Meeting


class MeetingCreate(CreateView):
    model = Meeting
    success_url = reverse_lazy('meeting_list')
    fields = ['topic', 'project', 'date', 'agenda']


class MettingUpdate(UpdateView):
    model = Meeting
    success_url = reverse_lazy('meeting_list')
    fields = ['topic', 'project', 'date', 'agenda']


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
