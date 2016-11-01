from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from projects.models import Project
from django.core.urlresolvers import reverse_lazy
from projects.form import ProjectForm


class ProjectList(ListView):
    model = Project


class ProjectCreate(CreateView):
    model = Project
    success_url = reverse_lazy('project_list')
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super(ProjectCreate, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super(ProjectCreate, self).form_valid(form)


class ProjectUpdate(UpdateView):
    model = Project
    success_url = reverse_lazy('project_list')
    fields = ['name', 'description']


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('project_list')
