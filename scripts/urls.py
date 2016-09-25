from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login2, name='login'),
    url(r'^auth/', views.auth_and_login,name='auth'),
    url(r'^signup/', views.sign_up, name='signup'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^signup_process/', views.sign_up_process, name='signup_process'),
    url(r'^error/', views.error, name='error'),
    url(r'^signin/', views.sign_in, name='signin'),
]