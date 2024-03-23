from django.contrib import admin
from django.urls import re_path, path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('apps.users.urls')),
    # re_path('login', views.login),
    # re_path('signup', views.signup),
    # re_path('test', views.test)
]
