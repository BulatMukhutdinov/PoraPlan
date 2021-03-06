import json

from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from meetings.form import MeetingForm
from meetings.models import Meeting, Agenda, Topic, MeetingFile


class MeetingList(ListView):
    template_name = "meetings.html"
    model = Meeting

    def get_context_data(self, **kwargs):
        context = super(MeetingList, self).get_context_data(**kwargs)
        context['meetings'] = Meeting.objects.all()
        context['topics'] = Topic.objects.all()
        # context['projects'] = Project.objects.all()
        return context


class MeetingCreate(CreateView):
    model = Meeting
    template_name = "meeting_create.html"
    success_url = reverse_lazy('meeting_list')
    form_class = MeetingForm

    def get_context_data(self, **kwargs):
        context = super(MeetingCreate, self).get_context_data(**kwargs)
        context['relativeMeetings'] = Meeting.objects.all
        return context

    def form_valid(self, form, **kwargs):
        topics = self.request.POST.get("agenda", "")
        relative_meeting = str(self.request.POST.get("relative_meeting", ""))
        topics = eval(json.dumps(json.loads(topics)))
        agenda = Agenda()
        agenda.time = 60
        agenda.save()

        files = self.request.FILES.getlist('file_list')
        for key, value in topics.iteritems():
            for topic in value:
                t = Topic()
                t.agenda = agenda
                for k, v in topic.iteritems():
                    if k == "name":
                        t.name = v
                    if k == "time":
                        t.time = v
                t.save()

        form.instance.agenda = agenda
        if len(relative_meeting) != 0:
            form.instance.relative_meeting = Meeting.objects.get(pk=relative_meeting)
        form.save()
        for f in files:
            meeting_file = MeetingFile()
            meeting_file.file = f
            meeting_file.meeting = form.instance
            meeting_file.save()
        return super(MeetingCreate, self).form_valid(form)


class MeetingUpdate(UpdateView):
    model = Meeting
    template_name = "meeting_create.html"
    success_url = reverse_lazy('meeting_list')
    form_class = MeetingForm

    def get_context_data(self, **kwargs):
        context = super(MeetingUpdate, self).get_context_data(**kwargs)
        meeting = self.object
        context['editMeetingId'] = meeting.id
        context['topics'] = Topic.objects.filter(agenda=meeting.agenda)
        if meeting.relative_meeting is not None:
            context['relativeMeeting'] = Meeting.objects.get(pk=meeting.relative_meeting.id)
        context['relativeMeetings'] = Meeting.objects.all

        return context

    def form_valid(self, form, **kwargs):
        form.save()
        return super(MeetingUpdate, self).form_valid(form)


class MeetingDelete(DeleteView):
    model = Meeting
    template_name = "meeting_delete.html"
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
