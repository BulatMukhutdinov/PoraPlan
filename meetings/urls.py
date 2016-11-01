from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', login_required(views.MeetingList.as_view()), name='meeting_list'),
    url(r'^new$', login_required(views.MeetingCreate.as_view()), name='meeting_new'),
    url(r'^edit/(?P<pk>\d+)$', login_required(views.MeetingUpdate.as_view()), name='meeting_edit'),
    url(r'^delete/(?P<pk>\d+)$', login_required(views.MeetingDelete.as_view()), name='meeting_delete'),

    url(r'^agenda$', login_required(views.AgendaList.as_view()), name='agenda_list'),
    url(r'^agenda/new$', login_required(views.AgendaCreate.as_view()), name='agenda_new'),
    url(r'^agenda/edit/(?P<pk>\d+)$', login_required(views.AgendaUpdate.as_view()), name='agenda_edit'),
    url(r'^agenda/delete/(?P<pk>\d+)$', login_required(views.AgendaDelete.as_view()), name='agenda_delete'),
]
