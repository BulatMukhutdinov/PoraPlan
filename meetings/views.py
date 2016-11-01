from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from meetings.form import MeetingForm
from meetings.models import Meeting, Agenda, Topic


class MeetingList(ListView):
    template_name = "meetings.html"
    model = Meeting


class MeetingCreate(CreateView):
    model = Meeting
    template_name = "meeting_create.html"
    success_url = reverse_lazy('meeting_list')
    form_class = MeetingForm

    def get_context_data(self, **kwargs):
        context = super(MeetingCreate, self).get_context_data(**kwargs)
        # context['meetingTypes'] = MeetingType.objects.all()
        # context['projects'] = Project.objects.all()
        return context

    def form_valid(self, form, **kwargs):
        topics = self.request.POST.get("agenda", "")
        topics = topics.split("\r\n")
        topics.pop(0)
        agenda = Agenda()
        agenda.time = 60
        agenda.save()
        for topic in topics:
            t = Topic()
            t.name = topic
            t.agenda = agenda
            t.save()
        form.instance.agenda = agenda
        form.save()
        return super(MeetingCreate, self).form_valid(form)


class MeetingUpdate(UpdateView):
    model = Meeting
    success_url = reverse_lazy('meeting_list')
    fields = ['topic', 'project', 'date']


class MeetingDelete(DeleteView):
    model = Meeting
    success_url = reverse_lazy('meeting_list')


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
