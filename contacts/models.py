from django.db import models

# Create your models here.
class Person_Data(models.Model):
    name = models.CharField(max_length=25),
    email = models.CharField(max_length=30),
    number = models.CharField(max_length=10),

    def __str__(self):
        return f"{self.name}"