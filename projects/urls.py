from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    url(r'^$', login_required(views.ProjectList.as_view()), name='project_list'),
    url(r'^send_invite$', login_required(views.send_invite), name='project_invite'),
    url(r'^view$', login_required(views.view), name='project_view'),
    url(r'^join$', login_required(views.join), name='project_join'),
    url(r'^new', login_required(views.ProjectCreate.as_view()), name='project_new'),
    url(r'^edit/(?P<pk>\d+)$', login_required(views.ProjectUpdate.as_view()), name='project_edit'),
    url(r'^delete/(?P<pk>\d+)$', login_required(views.ProjectDelete.as_view()), name='project_delete'),
]