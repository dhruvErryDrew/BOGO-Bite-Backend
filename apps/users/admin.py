from django.contrib import admin
# from django.contrib.auth.models import User
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'business'] 

admin.site.register(User, UserAdmin)