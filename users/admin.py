from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User , User_profile



admin.site.register(User , UserAdmin)
admin.site.register(User_profile)