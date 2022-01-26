from enum import auto
from django.db import models
from django.contrib.auth.models import AbstractUser

# Definition of User model
class User(AbstractUser):
    pass

# Definition of URL model
class Url(models.Model):
    short_url = models.CharField(verbose_name='Short URL',max_length=50, unique=True)
    long_url = models.CharField(verbose_name='Long URL',max_length=50)
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    