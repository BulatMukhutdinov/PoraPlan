from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from projects.models import Project
from django.core.urlresolvers import reverse_lazy


class ProjectList(ListView):
    model = Project


class ProjectCreate(CreateView):
    model = Project
    success_url = reverse_lazy('project_list')
    fields = ['name', 'description', 'deadline', "team_members", "team_users"]


class ProjectUpdate(UpdateView):
    model = Project
    success_url = reverse_lazy('project_list')
    fields = ['name', 'description']


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('project_list')
