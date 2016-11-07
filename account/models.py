from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from poraPlan.settings import STATIC_URL
from django.core.files.storage import FileSystemStorage

cs = FileSystemStorage(location='.'+STATIC_URL+'images/avatars')

class Account(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    birthday = models.CharField(max_length=100, null= True)
    avatar = models.ImageField(storage=cs, upload_to='images/avatars',null=True, blank=True)
    company = models.TextField(max_length=100,null=True)
    position = models.TextField(max_length=100,null = True)
    website = models.URLField(default='', blank=True,null=True)
    phone = models.CharField(max_length=20, blank=True,null=True, default='')
    city = models.CharField(max_length=100, default='',null=True, blank=True)
    country = models.CharField(max_length=100, default='',null=True, blank=True)


    def __str__(self):
        return "%s's profile" % self.user


