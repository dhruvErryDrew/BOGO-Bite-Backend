from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers

class User(AbstractUser):
    business = models.BooleanField(default=False)
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)

class UserSerializer(serializers.ModelSerializer):
    business = serializers.BooleanField(default=False)
    name = serializers.CharField(max_length = 100)
    location = serializers.CharField(max_length = 100)

    class Meta(object):
        model = User 
        fields = ['id', 'username', 'password', 'business', 'name', 'location']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make location required if business is true, and optional otherwise
        if self.context.get('request'):
            business = self.context['request'].data.get('business', False)
            self.fields['location'].required = business

    def validate(self, data):
        business = data.get('business', False)
        location = data.get('location', '')
        if business and not location:
            raise serializers.ValidationError("Location is required when business is true.")
        return data