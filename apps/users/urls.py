from django.contrib import admin
from django.urls import path, include
from . import views
from .views import UserListView



urlpatterns = [
    path('signup', views.signup),
    path('users/', UserListView.as_view(), name='user_list'),
    path('login', views.login)
]
