from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from users.models import ExtentUser
from django.contrib import admin

# Register your models here.

@admin.register(ExtentUser)
class ExtentUserAdmin(UserAdmin):
    pass
admin.site.unregister(Group)