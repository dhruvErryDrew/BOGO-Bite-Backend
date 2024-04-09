from django.contrib import admin
from .models import Coupon

class CouponAdmin(admin.ModelAdmin):
    list_display = ['business', 'title', 'desc', 'validThru'] 

admin.site.register(Coupon, CouponAdmin)