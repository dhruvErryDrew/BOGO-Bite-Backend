from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('addCoupon', views.addCoupon),
    path('getCoupons', views.getCoupons),
    path('coupons/', views.CouponList.as_view(), name='coupon-list')
    # path('login', views.login)
]
