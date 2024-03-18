from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    business = models.BooleanField(default=False)
    name = models.CharField(max_length = 100)