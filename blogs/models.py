import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    username        = models.CharField(max_length=75)
    email           = models.EmailField(max_length=75)
    passsword       = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class UserDetails(models.Model):
    user            = models.OneToOneField(User)
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    dob             = models.DateField()
    age             = models.IntegerField()
    description     = models.TextField()
    def __str__(self):
        return self.first_name

class Post(models.Model):
    author          = models.ForeignKey(User)
    title           = models.CharField(max_length=100)
    content         = models.TextField()
    slug            = models.SlugField()
    photo           = models.CharField(max_length=100)
    published_date  = models.DateTimeField('date published')
    views           = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days=1)
