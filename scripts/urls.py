from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login2, name='login'),
    url(r'^auth/', views.auth_and_login,name='auth'),
    url(r'^signup/', views.sign_up_in, name='signup'),
]