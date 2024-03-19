
from django.contrib import admin
from django.urls import re_path, path
from . import views

host = '10.142.124.237'

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test', views.test)
]
