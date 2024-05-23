from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_completed', 'created_at', 'updated_at']
    list_display_links = ['id', 'title', 'is_completed', 'created_at', 'updated_at']

admin.site.register(Todo, TodoAdmin)
