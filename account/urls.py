from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', login_required(views.AccountDetail.as_view()),name="account_detail"),
    url(r'^edit$', login_required(views.AccountUpdate.as_view()), name='account_update'),


]
