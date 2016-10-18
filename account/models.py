from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateTimeField(null=True)
    avatar = models.ImageField(null=True)
    company = models.TextField(max_length=100)
    position = models.TextField(max_length=100)
