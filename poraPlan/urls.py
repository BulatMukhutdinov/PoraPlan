from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # url(r'^', include('authorization.urls')),
    url(r'^meetings/', include('meetings.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^authorization/', include('authorization.urls')),
    url(r'^', include('home.urls')),
    url(r'^admin/', admin.site.urls),
]
