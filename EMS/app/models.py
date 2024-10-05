from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Account(models.Model):
    username=models.CharField(max_length=10)
    pno=models.CharField(max_length=13)

    def __str__(self):
        return self.username.username
    


class Eventcreation(models.Model):
    creat_events=models.TextField()
    event_title=models.TextField()
    description=models.TextField()
    date=models.DateField()
    time=models.TimeField()
    location=models.TextField()


    def __str__(self):
        return self.text[:10]
