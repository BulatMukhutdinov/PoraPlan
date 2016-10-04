from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ProjectList.as_view(), name='project_list'),
    url(r'new', views.ProjectCreate.as_view(), name='project_new'),
    url(r'^edit/(?P<pk>\d+)$', views.ProjectUpdate.as_view(), name='project_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.ProjectDelete.as_view(), name='project_delete'),
]
