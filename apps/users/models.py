from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers

class User(AbstractUser):
    business = models.BooleanField(default=False)
    name = models.CharField(max_length = 100)

class UserSerializer(serializers.ModelSerializer):
    business = serializers.BooleanField(default=False)
    name = serializers.CharField(max_length = 100)
    class Meta(object):
        model = User 
        fields = ['id', 'username', 'password', 'business', 'name']