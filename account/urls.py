from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', login_required(views.AccountView.as_view()),name="account_view"),
]
