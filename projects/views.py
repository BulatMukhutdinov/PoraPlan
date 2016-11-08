from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from projects.models import Project, TeamMembers
from django.core.urlresolvers import reverse_lazy
from projects.form import ProjectForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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


def join(request):
    pk = request.GET["project_id"]
    obj = Project.objects.get(pk=pk)

    team_member = TeamMembers()
    User.objects.get_by_natural_key(request.GET["email"])
    team_member.member = team_member
    team_member.save()
    obj.team_members.add(team_member)

    return None


def send_invite(request):

    u = "ddddddddddddddddd"

    send_mail(
        subject='PORAPLAN.PRO: You have been invited to project',
        #html_message='Click <a href="'+u+'">here</a> to join. Hello world!!!!!!',
        message="asdfasdfasdfasd",
        from_email='support@poraplan.pro',
        recipient_list=['limit-speed@yandex.ru']
    )

    plaintext = ""#get_template('email.txt')
    htmly = ""#get_template('email.html')

    d = Context({'username': "Igor Bobko"})

    subject, from_email, to = 'hello', 'support@poraplan.ru', 'iibobko@gmail.com'
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return None

