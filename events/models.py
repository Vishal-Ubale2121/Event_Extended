from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.DateField()

    class Meta:
        db_table = 'event'


class Team(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,)
    team_name = models.CharField(max_length=200)

    class Meta:
        db_table = 'team'


class Member(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE,)
    team = models.ForeignKey(Team, on_delete=models.CASCADE,)
    is_captain = models.BooleanField()

    class Meta:
        db_table = 'member'

##################################################################

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )


Choice = [
    ('music', 'Music'),
    ('play', 'Play'),
    ('dance', 'Dance'),
    ('party', 'Party'),
    ]

class Mood(models.Model):

    Team_Name = models.CharField(max_length=120)


    class Meta:
        db_table = "mood"



class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    file = models.FileField(upload_to='documents/', blank=True)

    def __str__(self):
        return self.title