from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.PlaceList.as_view(), name='place_list'),
    url(r'new', views.PlaceCreate.as_view(), name='place_new'),
    url(r'^edit/(?P<pk>\d+)$', views.PlaceUpdate.as_view(), name='place_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.PlaceDelete.as_view(), name='place_delete'),
]
