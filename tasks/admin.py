from django.contrib import admin

from .models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'author', 'executor', 'created_at')
    search_fields = ('name',)
    list_filter = ('status', 'executor')
