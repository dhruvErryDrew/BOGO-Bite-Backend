from django.contrib import admin
from django.urls import path, include
from .views import CouponListView, CouponDetailView
from apps.coupons import views

urlpatterns = [
    path('addCoupon/', views.addCoupon),
    path('getCoupons/', views.getCoupons),
    path('coupons/', views.CouponList.as_view(), name='coupon-list'),
    path('coupons/<int:pk>/', CouponDetailView.as_view(), name='coupon-detail'),
    path('login/', views.login),
]