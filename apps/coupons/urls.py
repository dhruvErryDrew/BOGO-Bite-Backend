from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('addCoupon', views.addCoupon),
    path('getCoupons', views.getCoupons),
    # path('login', views.login)
]
