from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    phonenumber = models.CharField(max_length=20,blank=False,null=False)

class Contacts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)
    name = models.CharField(max_length=25,blank=False,null=False)
    email = models.CharField(max_length=30,blank=False,null=False)
    number = models.CharField(max_length=20,blank=False,null=False)

    ROLE_CHOICES = [
        ('user','User'),
    ]
    role = models.CharField(max_length=10,choices=ROLE_CHOICES,default='user')

    def __str__(self):
        return f"{self.name}"