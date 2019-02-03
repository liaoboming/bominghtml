from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    fullName = models.CharField(max_length=128)
    

    def __str__(self):
        return self.fullName 
