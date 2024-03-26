from django.db import models
from rest_framework import serializers

class Coupon(models.Model):
    business = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    desc = models.TextField()
    validThru = models.DateField()

class CouponSerializer(serializers.ModelSerializer):
    business = serializers.CharField(max_length = 100)
    title = serializers.CharField(max_length = 100)
    desc = serializers.CharField()
    validThru = serializers.DateField()
    class Meta(object):
        model = Coupon 
        fields = ['business', 'title', 'desc', 'validThru']