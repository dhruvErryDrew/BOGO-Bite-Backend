from django.contrib import admin
from django.urls import re_path, path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('apps.users.urls')),
    path('coupons/', include('apps.coupons.urls'))
]
