from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Place(models.Model):
    room_number = models.IntegerField()
    white_board = models.BooleanField()
    black_board = models.BooleanField()

    conference_equipment = models.BooleanField()
    start_date = models.DateTimeField()
    duration = models.IntegerField(validators=[MinValueValidator(0),
                                               MaxValueValidator(300)])
    num_of_persons = models.IntegerField(validators=[MinValueValidator(0),
                                               MaxValueValidator(30)])

