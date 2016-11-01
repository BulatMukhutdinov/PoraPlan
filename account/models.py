from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from datetime import date



class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    birthday = models.DateField(default=date.today, null= True)
    avatar = models.ImageField(upload_to='/images/',default = '/images/None/no-photo.png')
    company = models.TextField(max_length=100,null=True)
    position = models.TextField(max_length=100,null = True)


