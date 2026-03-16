from django.contrib import admin

from .models import Labels


@admin.register(Labels)
class LabelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')
    search_fields = ('name',)
