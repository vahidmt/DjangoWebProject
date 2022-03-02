from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import admins


admin.site.register(admins)




