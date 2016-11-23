from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^auth/', views.auth_and_login, name='auth'),
    url(r'^sign_up/', views.sign_up, name='sign_up'),
    url(r'^signup_process/', views.sign_up_process, name='signup_process'),
    url(r'^sign_in/$', views.sign_in, name='sign_in'),
    url(r'^log_out/', views.log_out, name='log_out'),
]
