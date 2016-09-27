from django.db import models


# Create your models here.

class Account(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

    def __str__(self):
        name = "Mr. "
        if self.gender == 'F':
            name = "Mrs. "
        return name + self.first_name + " " + self.last_name
