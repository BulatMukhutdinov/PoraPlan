from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.MeetingList.as_view(), name='meeting_list'),
    url(r'^new$', views.MeetingCreate.as_view(), name='meeting_new'),
    url(r'^edit/(?P<pk>\d+)$', views.MettingUpdate.as_view(), name='meeting_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.MeetingDelete.as_view(), name='meeting_delete'),

    url(r'^agenda$', views.AgendaList.as_view(), name='agenda_list'),
    url(r'^agenda/new$', views.AgendaCreate.as_view(), name='agenda_new'),
    url(r'^agenda/edit/(?P<pk>\d+)$', views.AgendaUpdate.as_view(), name='agenda_edit'),
    url(r'^agenda/delete/(?P<pk>\d+)$', views.AgendaDelete.as_view(), name='agenda_delete'),
]
