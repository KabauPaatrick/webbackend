# locations/admin.py
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Location

@admin.register(Location)
class LocationAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'name')
    list_display_links = ('indented_title',)
    search_fields = ('name',)


# Register your models here.
