from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=25,blank=False,null=False),
    email = models.CharField(max_length=30,blank=False,null=False),
    number = models.CharField(max_length=20,blank=False,null=False),

    ROLE_CHOICES = [
        ('user','User'),
    ]
    role = models.CharField(max_length=10,choices=ROLE_CHOICES,default='user')

    def __str__(self):
        return f"{self.name}"