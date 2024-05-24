from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CustomUser

admin.site.unregister(Group)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'role', 'date_joined']
    list_display_links = ['id', 'username', 'email', 'role', 'date_joined']

admin.site.register(CustomUser, CustomUserAdmin)
