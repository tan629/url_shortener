from enum import auto
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# Create your models here.
class Url(models.Model):
    short_url = models.CharField(max_length=50, unique=True)
    long_url = models.CharField(max_length=50)
    user_id = models.ForeignKey('User',on_delete=models.CASCADE,)
    date_created = models.DateTimeField(auto_now=True)
    