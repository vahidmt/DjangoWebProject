from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField



# Create your models here.
    
class info_site(models.Model):
    title = models.CharField(max_length=15)
class admins(models.Model):
    name_admin = models.CharField(max_length=200)
    def __str__(self):
        return self.name_admin