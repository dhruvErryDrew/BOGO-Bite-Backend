from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('addCoupon', views.addCoupon),
    # path('login', views.login)
]
