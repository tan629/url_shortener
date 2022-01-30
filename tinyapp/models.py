from enum import auto
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Definition of User model
class User(AbstractUser):
    def __str__(self):
        return self.first_name + " " + self.last_name

# Definition of URL model
class Url(models.Model):
    short_url = models.CharField(verbose_name='Short URL', max_length=6,unique=True)
    long_url = models.URLField(verbose_name='Long URL',max_length=500)
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    slug_field = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.short_url

    def get_absolute_url(self):
       return reverse('url-detail', kwargs={'pk':self.pk,'slug': self.slug_field})

    