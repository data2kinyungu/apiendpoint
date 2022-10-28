from django.db import models

# Create your models here.
class Task(models.Model):
    slack_username = models.CharField(max_length=100)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.CharField(max_length=150)