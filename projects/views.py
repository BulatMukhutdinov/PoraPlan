from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from account.models import Account
from meetings.models import Meeting
from projects.form import ProjectForm
from projects.models import Project, TeamMembers, ProjectRoles


class ProjectList(ListView):
    model = Project


class ProjectCreate(CreateView):
    model = Project
    success_url = reverse_lazy('project_list')
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super(ProjectCreate, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['acs'] = Account.objects.all()

        return context

    def form_valid(self, form):


        role = ProjectRoles.objects.get(name="Participator")
        team_member = TeamMembers()
        team_member.member = User.objects.get(username="limit-speed@yandex.ru")
        team_member.role = role
        team_member.save()

        form.save()
        form.instance.team_members.add(team_member)
        form.save()

        user = User.objects.get(username="limit-speed@yandex.ru")

        plaintext = get_template('email.txt')
        htmly = get_template('email.html')
        d = Context(
            {'username': "Igor Bobko",
             'project_id': form.instance.pk,
             'user_email': "limit-speed@yandex.ru",
             }
        )

        subject = 'PORAPLAN.PRO: You have been invited to project'
        from_email, to = 'support@poraplan.pro', user.email
        text_content = plaintext.render(d)
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()



        return super(ProjectCreate, self).form_valid(form)


class ProjectUpdate(UpdateView):
    model = Project
    success_url = reverse_lazy('project_list')
    fields = ['name', 'description']


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('project_list')

def view(request):
    pk = request.GET["project_id"]

    meetings = Meeting.objects.filter(project=Project.objects.get(pk=pk))
    context = {
        "project": Project.objects.get(pk=pk),
        "meetings": meetings
    }

    return render(request,"project.html",context)


def join(request):
    pk = request.GET["project_id"]
    email = request.GET["email"]

    obj = Project.objects.get(pk=pk)

    role = ProjectRoles.objects.get(name="Participator")



    team_member = TeamMembers()
    team_member.member = User.objects.get(username=email)
    team_member.role = role
    team_member.save()
    obj.team_members.add(team_member)
    obj.save()

    context = {
        "project" : obj,

    }

    return render(request,"joined.html",context)


def send_invite(request):

    user = User.objects.get(username=request.GET["email"])

    plaintext = get_template('email.txt')
    htmly = get_template('email.html')
    d = Context(
        {'username': "Igor Bobko",
         'project_id': request.GET["project_id"],
         'user_email': request.GET["email"],
         }
    )

    subject = 'PORAPLAN.PRO: You have been invited to project'
    from_email, to = 'support@poraplan.pro', user.email
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return HttpResponse("", "text/plain", 200)
